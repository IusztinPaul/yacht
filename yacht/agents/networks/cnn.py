# [
#     {
#         'activation_function': 'relu', 'filter_number': 3, 'filter_shape': [1, 2], 'padding': 'valid',
#         'regularizer': None,
#         'strides': [1, 1], 'type': 'ConvLayer', 'weight_decay': 0.0
#     },
#     {
#         'activation_function': 'relu', 'filter_number': 10, 'regularizer': 'L2', 'type': 'EIIE_Dense',
#         'weight_decay': 5e-09
#     },
#     {
#         'regularizer': 'L2', 'type': 'EIIE_Output_WithW', 'weight_decay': 5e-08
#     }
# ]
import torch

from torch import nn

from agents.networks import layers


# class _EIIECNN(Model):
#     def __init__(self):
#         super().__init__(name='EIIE_CNN')
#
#         # self.conv_2d = tf_layers.Conv2D(
#         #     3,
#         #     kernel_size=(1, 2),
#         #     strides=(1, 1),
#         #     padding='valid',
#         #     activation='relu',
#         #     kernel_regularizer=None,
#         #     # TODO: See how to add weight decay
#         #     # weight_decay=0.0
#         # )
#         # self.eiie_dense = layers.EIIEDense(
#         #     10,
#         #     'relu',
#         #     'l2',
#         #     5e-09
#         # )
#         #
#         # self.eiie_output_with_w = layers.EIIEOutputWithW(
#         #     # kernel_regularizer='l2',
#         #     # TODO: See how to add weight decay
#         #     # weight_decay=5e-08
#         # )
#
#     # Tensor("Placeholder_1:0", shape=(?, 3, 11, 31), dtype=float32)
#     def call(self, input_tensor, previous_w, training=False):
#         # tensor = tf.transpose(input_tensor, (0, 2, 3, 1))
#         # tensor = tensor / tensor[:, :, -1, 0, None, None]
#         #
#         # tensor = self.conv_2d(tensor)
#         # tensor = self.eiie_dense(tensor)
#         # tensor = self.eiie_output_with_w(tensor, previous_w)
#         #
#         # return tensor
#         return input_tensor


class EIIECNN(nn.Module):
    def __init__(self, name='EIIE_CNN'):
        super().__init__()
        self.name = name

        self.conv_2d = nn.Conv2d(
            in_channels=3,
            out_channels=3,
            kernel_size=(1, 2),
            stride=(1, 1),
            padding=(0, 0)
        )
        self.eiie_dense = layers.EIIEDense(
            input_channels=3,
            output_channels=10,
            kernel_width=30
        )
        self.eiie_output_with_w = layers.EIIEOutputWithW(
            input_channels=11
        )

    def forward(self, input_tensor, previous_w):
        batch, features, assets, window = input_tensor.shape

        last_window_item_closing_prices = input_tensor[:, 0, :, -1]
        last_window_item_closing_prices = last_window_item_closing_prices.reshape(batch, 1, assets, 1)

        tensor = input_tensor / last_window_item_closing_prices

        tensor = self.conv_2d(tensor)
        tensor = self.eiie_dense(tensor)
        tensor = self.eiie_output_with_w(tensor, previous_w)

        return tensor


if __name__ == '__main__':
    eiie_network = EIIECNN().to('cuda')

    result = eiie_network(
        torch.ones((1, 3, 11, 31)).to('cuda'),
        torch.ones((1, 11)).to('cuda')
    )
    print(result)
