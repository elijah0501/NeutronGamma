import torch.nn
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        # 先运行nn.Module的初始化函数
        super(Net, self).__init__()
        self.conv = torch.nn.Sequential(
            nn.Conv1d(1, 128, 3, padding=1),
            nn.AvgPool1d(2, stride=2),  # 50
            nn.Sigmoid(),
            nn.Conv1d(128, 256, 3, padding=1),
            nn.AvgPool1d(2, stride=2),  # 25
            nn.Sigmoid(),
            nn.Conv1d(256, 512, 3, padding=1),
            nn.AvgPool1d(3, stride=2),  # 12
            nn.Sigmoid(),
            nn.Conv1d(512, 256, 3, padding=1),
            nn.AvgPool1d(2, stride=2),  # 6
            nn.Sigmoid(),
            nn.Conv1d(256, 128, 3, padding=1),
            nn.AvgPool1d(2, stride=2),  # 3
            nn.Sigmoid(),
        )
        # 全连接后接softmax
        self.fc = nn.Linear(384, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # 卷积层，分别是二维卷积->sigmoid激励->池化
        out = self.conv(x)
        out = F.sigmoid(out)
        # 将特征的维度进行变化(batchSize*filterDim*featureDim*featureDim->batchSize*flat_features)
        out = out.view(-1, self.num_flat_features(out))
        last_layer_feature = out
        # 全连接层和softmax处理
        out = self.fc(out)
        out = self.sigmoid(out)
        return out, last_layer_feature


    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
