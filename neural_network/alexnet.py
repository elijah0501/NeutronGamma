# coding:utf8

import torch
import torch.nn as nn


class AlexNet(nn.Module):
    def __init__(self, num_class=4096):
        super(AlexNet, self).__init__()
        self.num_class = num_class
        self.create_model()

    def create_model(self):
        self.conv1 = nn.Sequential(nn.Conv1d(1, 128, 3, padding=1),
                                   nn.Sigmoid(),
                                   nn.MaxPool1d(2, stride=2))
        self.conv2 = nn.Sequential(nn.Conv1d(128, 512, 3, padding=1),
                                   nn.Sigmoid(),
                                   nn.MaxPool1d(2, stride=2)
                                   )
        self.conv3 = nn.Sequential(nn.Conv1d(512, 1024, 3, padding=1),
                                   nn.Sigmoid(),)
        self.conv4 = nn.Sequential(nn.Conv1d(1024, 256, 3, padding=1),
                                   nn.Sigmoid(),)
        self.conv5 = nn.Sequential(nn.Conv1d(256, 128, 3, padding=1),
                                   nn.Sigmoid(),
                                   nn.MaxPool1d(2, stride=2))

        self.fc6 = nn.Sequential(nn.Linear(1536, 2),
                                 nn.Dropout(p=0.6))
        self.fc7 = nn.Sequential(nn.Linear(2, self.num_class))

    def forward(self, x):
        batch_size = x.size()[0]
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = x.view(batch_size, -1)
        last_layer_feature = x
        x = self.fc6(x)
        x = self.fc7(x)
        return x, last_layer_feature


if __name__ == '__main__':
    input_tensor = torch.randn((1, 1, 100))
    input_var = torch.autograd.Variable(input_tensor)

    model = AlexNet(num_class=2)
    output = model(input_var)
    print(output)
