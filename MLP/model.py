import torch
from torch import nn


class MLP(nn.Module):
    def __init__(self, input_dim, class_number):
        super(MLP, self).__init__()
        self.class_number = class_number
        self.fc1 = torch.nn.Linear(in_features=100, out_features=1024)
        self.fc2 = torch.nn.Linear(in_features=1024, out_features=512)
        self.output_layer = torch.nn.Linear(in_features=512, out_features=class_number)

    def forward(self, x):
        y = torch.sigmoid(self.fc1(x))
        y = torch.sigmoid(self.fc2(y))
        last_layer_feature = y
        output = self.output_layer(y)
        return output, last_layer_feature


if __name__ == '__main__':
    x = torch.rand((100, 100), )
    # print(x)
    model = MLP(input_dim=100, class_number=2)
    y = model(x)
    print(y)
