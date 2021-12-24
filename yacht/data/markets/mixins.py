from datetime import datetime
from typing import List, Any, Union

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from stockstats import StockDataFrame

from yacht.data.markets import Market


class TechnicalIndicatorMixin:
    def __init__(self, technical_indicators: List[str], *args, **kwargs):
        assert Market in type(self).mro(), \
            '"TechnicalIndicatorMixin" works only with "Market" objects.'

        super().__init__(*args, **kwargs)

        self.technical_indicators = technical_indicators
        self.data_features = self.features
        self.features = self.technical_indicators + self.features

    def is_cached(
            self,
            ticker: str,
            interval: str,
            start: datetime,
            end: datetime
    ) -> bool:
        value = super().is_cached(ticker, interval, start, end)

        if value is False:
            return False

        key = self.create_key(ticker, interval)
        data_columns = set(self.connection[key].columns)

        return set(self.technical_indicators).issubset(data_columns) and value

    def process_request(self, data: Union[List[List[Any]], pd.DataFrame]) -> pd.DataFrame:
        df = super().process_request(data)

        stock = StockDataFrame.retype(df.copy())
        for technical_indicator_name in self.technical_indicators:
            oscillator_data = stock[technical_indicator_name]
            df[technical_indicator_name] = oscillator_data

        return df


class TargetPriceMixin:
    def process_request(self, data: Union[List[List[Any]], pd.DataFrame]) -> pd.DataFrame:
        df = super().process_request(data)

        df['TP'] = df.apply(func=self.compute_target_price, axis=1)

        return df

    @classmethod
    def compute_target_price(cls, row: pd.Series):
        # Because there is no VWAP field in the yahoo data,
        # a method similar to Simpson integration is used to approximate VWAP.
        return (row['Open'] + 2 * row['High'] + 2 * row['Low'] + row['Close']) / 6


class LogDifferenceMixin:
    def process_request(self, data: Union[List[List[Any]], pd.DataFrame]) -> pd.DataFrame:
        df = super().process_request(data)

        df_log_dif_t = df[self.DOWNLOAD_MANDATORY_FEATURES].copy()
        df_log_dif_t_minus_1 = df_log_dif_t.shift(1)
        # Add a small value to both sides to avoid division by 0 & log of 0.
        df_log_diff = (df_log_dif_t + 1e-7) / (df_log_dif_t_minus_1 + 1e-7)
        df_log_diff = df_log_diff.apply(np.log)
        df_log_diff.fillna(method='bfill', inplace=True, axis=0)
        df_log_diff.fillna(method='ffill', inplace=True, axis=0)

        log_diff_column_mappings = {column: f'{column}LogDiff' for column in self.DOWNLOAD_MANDATORY_FEATURES}
        df_log_diff.rename(columns=log_diff_column_mappings, inplace=True)

        df = pd.concat([df, df_log_diff], axis=1)

        return df


class FracDiffMixin:
    def process_request(self, data: Union[List[List[Any]], pd.DataFrame]) -> pd.DataFrame:
        df = super().process_request(data)

        # TODO: Inject this value from the config
        # TODO: Make FracDiff only on the train set.
        window_size = 5

        data_to_process = df[self.DOWNLOAD_MANDATORY_FEATURES].copy()
        data_to_process = data_to_process.apply(np.log)
        d_value = self.find_d_value(data=data_to_process, size=window_size)

        assert d_value is not None, 'Could not find d_value'

        data_to_process = self.frac_diff_fixed_ffd(series=data_to_process, d=d_value, size=window_size)
        data_to_process.bfill(axis='rows', inplace=True)
        data_to_process.ffill(axis='rows', inplace=True)

        log_diff_column_mappings = {column: f'{column}FracDiff' for column in self.DOWNLOAD_MANDATORY_FEATURES}
        data_to_process.rename(columns=log_diff_column_mappings, inplace=True)

        df = pd.concat([df, data_to_process], axis=1)

        return df

    @classmethod
    def find_d_value(cls, data: pd.DataFrame, size: int):
        out = pd.DataFrame(columns=['adfStat', 'pVal', 'lags', 'nObs', '95% conf', 'corr'])
        for d in np.linspace(0, 2, 21):
            df1 = data[['Close']].resample('1D').last()
            df2 = cls.frac_diff_fixed_ffd(df1, d, size=size)
            corr = np.corrcoef(df1.loc[df2.index, 'Close'], df2['Close'])[0, 1]
            df2 = adfuller(df2['Close'], maxlag=1, regression='c', autolag=None)

            out.loc[d] = list(df2[:4]) + [df2[4]['5%']] + [corr]
        
        return cls._parse_d_values(out)

    @classmethod
    def _parse_d_values(cls, results):
        # adfStat values are within [0, -inf]. When a adfStat value crosses the 95% conf border
        # we consider that we have found the d_value which makes the data stationary.
        conf_95 = results['95% conf'].mean()
        for d_value, row in results.iterrows():
            if row['adfStat'] <= conf_95:
                return d_value

        return None

    @classmethod
    def frac_diff_fixed_ffd(cls, series, d, size):
        # Constant width window
        w = cls.get_fixed_weights_ffd(d, size)
        width = len(w) - 1
        df = {}
        for name in series.columns:
            seriesF = series[[name]].fillna(method='ffill').dropna()
            df_ = pd.Series(dtype=np.float32)
            for iloc1 in range(width, seriesF.shape[0]):
                loc0 = seriesF.index[iloc1 - width]
                loc1 = seriesF.index[iloc1]
                if not np.isfinite(series.loc[loc1, name]):
                    # Exclude NaNs
                    continue

                df_[loc1] = np.dot(w.T, seriesF.loc[loc0:loc1]).item()
            df[name] = df_.copy(deep=True)
        df = pd.concat(df, axis=1)

        return df

    @classmethod
    def get_fixed_weights_ffd(cls, d, size):
        w = [1.]
        for k in range(1, size):
            w_ = -w[-1] / k * (d - k + 1)
            w.append(w_)
        w = np.array(w[::-1]).reshape(-1, 1)

        return w
