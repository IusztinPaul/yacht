import itertools
import time
from copy import copy
from typing import Set

from tqdm import tqdm

from .base import *
from .day_frequency import DayFrequencyDataset
from .samplers import SampleAssetDataset
from .multi_frequency import *

import yacht.utils as utils

from yacht.config import Config
from yacht.data import indexes
from yacht.data.markets import build_market
from yacht.data.renderers import TrainTestSplitRenderer
from yacht.data.scalers import build_scaler
from yacht import Mode


dataset_registry = {
    'DayMultiFrequencyDataset': DayMultiFrequencyDataset,
    'DayFrequencyDataset': DayFrequencyDataset
}


def build_dataset(
        config: Config,
        logger: Logger,
        storage_dir,
        mode: Mode
) -> Optional[SampleAssetDataset]:
    start_building_data_time = time.time()

    input_config = config.input
    dataset_cls = dataset_registry[input_config.dataset]

    tickers = build_tickers(config, mode)
    market = build_market(config, logger, storage_dir)

    train_split, validation_split, backtest_split = utils.split(
        input_config.start,
        input_config.end,
        input_config.validation_split_ratio,
        input_config.backtest_split_ratio,
        input_config.embargo_ratio,
        input_config.include_weekends
    )

    # Download the whole requested interval in one shot for further processing & rendering.
    market.download(
        tickers,
        interval='1d',
        start=utils.string_to_datetime(input_config.start),
        end=utils.string_to_datetime(input_config.end),
        flexible_start=True
    )
    # Render split only for backtest tickers.
    if not mode.is_trainable():
        data = dict()
        for ticker in tickers:
            data[ticker] = market.get(
                ticker,
                '1d',
                utils.string_to_datetime(input_config.start),
                utils.string_to_datetime(input_config.end),
                flexible_start=True
            )

        # Render de train-test split in rescaled mode.
        renderer = TrainTestSplitRenderer(
            data=data,
            train_split=train_split,
            validation_split=validation_split,
            backtest_split=backtest_split,
            rescale=True
        )
        renderer.render()
        renderer.save(utils.build_graphics_path(storage_dir, f'{mode.value}_train_test_split_rescaled.png'))
        renderer.close()

        # Render de train-test split with original values.
        renderer = TrainTestSplitRenderer(
            data=data,
            train_split=train_split,
            validation_split=validation_split,
            backtest_split=backtest_split,
            rescale=False
        )
        renderer.render()
        renderer.save(utils.build_graphics_path(storage_dir, f'{mode.value}_train_test_split.png'))
        renderer.close()

    logger.info(f'Building datasets for: {mode.value}')
    logger.info(f'Loading the following assets:')
    logger.info(tickers)
    if mode.is_trainable() or mode.is_backtest_on_train():
        logger.info(f'Train split: {train_split[0]} - {train_split[1]}')
        start = train_split[0]
        end = train_split[1]
    elif mode.is_validation():
        logger.info(f'Validation split: {validation_split[0]} - {validation_split[1]}')
        start = validation_split[0]
        end = validation_split[1]
    else:
        logger.info(f'Backtest split: {backtest_split[0]} - {backtest_split[1]}')
        start = backtest_split[0]
        end = backtest_split[1]

    # Datasets will expand their data range with -window_size on the left side of the interval.
    start = utils.adjust_period_to_window(
        datetime_point=start,
        window_size=input_config.window_size,
        action='+',
        include_weekends=input_config.include_weekends
    )
    periods = utils.compute_periods(
        start=start,
        end=end,
        include_weekends=input_config.include_weekends,
        period_length=input_config.period_length,
        include_edges=False
    )

    total_num_periods = len(periods) * len(list(itertools.combinations(tickers, config.input.num_assets_per_dataset)))
    logger.info('Creating datasets...')
    logger.info(f'Total estimated num datasets: {total_num_periods}')

    if len(periods) == 0:
        return None

    render_intervals = utils.compute_render_periods(list(config.input.render_periods))
    num_skipped_periods = 0
    datasets: List[Union[SingleAssetDataset, MultiAssetDataset]] = []
    for (period_start, period_end) in tqdm(periods, desc='Num periods'):
        dataset_period = DatasetPeriod(
            start=period_start,
            end=period_end,
            window_size=input_config.window_size,
            include_weekends=input_config.include_weekends
        )
        for dataset_tickers in itertools.combinations(tickers, config.input.num_assets_per_dataset):
            # If the period is cached, after a download operation was tried, it means it is available for usage.
            tickers_validity = [
                market.is_cached(ticker, '1d', dataset_period.start, dataset_period.end)
                for ticker in dataset_tickers
            ]
            if all(tickers_validity) is False:
                num_skipped_periods += 1
                continue

            dataset_period = copy(dataset_period)
            single_asset_datasets: List[SingleAssetDataset] = []
            for ticker in dataset_tickers:
                scaler = build_scaler(
                    config=config,
                    ticker=ticker
                )
                Scaler.fit_on(
                    scaler=scaler,
                    market=market,
                    train_start=train_split[0],
                    train_end=train_split[1],
                    interval=config.input.scale_on_interval
                )

                single_asset_datasets.append(
                    dataset_cls(
                        ticker=ticker,
                        market=market,
                        intervals=list(input_config.intervals),
                        features=list(input_config.features) + list(input_config.technical_indicators),
                        decision_price_feature=input_config.decision_price_feature,
                        period=dataset_period,
                        render_intervals=render_intervals,
                        mode=mode,
                        logger=logger,
                        scaler=scaler,
                        window_size=input_config.window_size
                    )
                )

            dataset = MultiAssetDataset(
                datasets=single_asset_datasets,
                market=market,
                intervals=list(input_config.intervals),
                features=list(input_config.features) + list(input_config.technical_indicators),
                decision_price_feature=input_config.decision_price_feature,
                period=dataset_period,
                render_intervals=render_intervals,
                mode=mode,
                logger=logger,
                window_size=input_config.window_size
            )
            datasets.append(dataset)

    days_per_period = len(utils.compute_period_range(
        start=periods[0][0],
        end=periods[0][1],
        include_weekends=input_config.include_weekends
    ))
    usable_num_datasets = total_num_periods - num_skipped_periods
    logger.info(f'Skipped {num_skipped_periods} / {total_num_periods} datasets.')
    logger.info(f'A total of {usable_num_datasets} datasets were created.')
    logger.info(f'Which is equal to a total of {usable_num_datasets * days_per_period} timesteps.')
    logger.info(f'Datasets built in {time.time() - start_building_data_time:.2f} seconds.')

    if usable_num_datasets == 0:
        return None

    sample_dataset_period = DatasetPeriod(
        start=start,
        end=end,
        window_size=input_config.window_size,
        include_weekends=input_config.include_weekends
    )
    return SampleAssetDataset(
        datasets=datasets,
        market=market,
        intervals=list(input_config.intervals),
        features=list(input_config.features) + list(input_config.technical_indicators),
        decision_price_feature=input_config.decision_price_feature,
        period=sample_dataset_period,
        render_intervals=render_intervals,
        mode=mode,
        logger=logger,
        window_size=input_config.window_size,
        default_index=0,
        shuffle=mode.is_trainable()
    )


def build_tickers(config: Config, mode: Mode) -> Set[str]:
    input_config = config.input

    if mode.is_trainable():
        if mode.is_fine_tuning():
            tickers = list(input_config.fine_tune_tickers)
        else:
            tickers = list(input_config.tickers)
    else:
        tickers = list(input_config.backtest.tickers)

    assert len(tickers) > 0
    assert len(tickers) >= config.input.num_assets_per_dataset, 'Cannot create a dataset with less tickers than asked.'

    if 'S&P500' in tickers:
        tickers.remove('S&P500')
        tickers.extend(indexes.SP_500_TICKERS)
    if 'NASDAQ100' in tickers:
        tickers.remove('NASDAQ100')
        tickers.extend(indexes.NASDAQ_100_TICKERS)
    if 'DOW30' in tickers:
        tickers.remove('DOW30')
        tickers.extend(indexes.DOW_30_TICKERS)
    if 'RUSSELL2000' in tickers:
        tickers.remove('RUSSELL2000')
        tickers.extend(indexes.RUSSELL_2000_TICKERS)

    return set(tickers)


def build_dataset_wrapper(dataset: AssetDataset, indices: List[int]) -> Union[IndexedDatasetMixin, AssetDataset]:
    dataset_class_name = dataset.__class__.__name__
    dataset_class_name = f'Indexed{dataset_class_name}'
    dataset_class = dataset_registry[dataset_class_name]

    return dataset_class(
        dataset.market,
        dataset.ticker,
        dataset.intervals,
        dataset.features,
        dataset.start,
        dataset.end,
        dataset.price_normalizer,
        dataset.other_normalizer,
        dataset.window_size,
        dataset.data,
        indices
    )
