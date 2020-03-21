import torch as t
import torch.nn as nn
import numpy as np

class Conv3D(nn.Module):
    def __init__(self, c, o, kernel=3, stride=1, padding=1, g=1):
        super(Conv3D, self).__init__()
        if padding == None:
            padding = (kernel_size - 1) // 2
        self.conv = nn.Conv3d(c, o, kernel_size=kernel, stride=stride, padding=padding, groups=g, )
        # self.bn = nn.BatchNorm3d(o)
        self.bn = nn.InstanceNorm3d(o)
        self.relu = nn.LeakyReLU(negative_slope=1e-2, inplace=True)

    def forward(self, x):
        h = self.conv(x)
        h = self.bn(h)
        h = self.relu(h)

        return h



class No_new_net(nn.Module):
    def __init__(self):
        super(No_new_net, self).__init__()

        self.layer1 = nn.Sequential(
            Conv3D(4, 30),
            Conv3D(30, 30)
        )

        self.layer2 = nn.Sequential(
            Conv3D(30, 60),
            Conv3D(60, 60)
        )

        self.layer3 = nn.Sequential(
            Conv3D(60, 120),
            Conv3D(120, 120)
        )

        self.layer4 = nn.Sequential(
            Conv3D(120, 240),
            Conv3D(240, 240)
        )

        self.layer5 = nn.Sequential(
            Conv3D(240, 480),
            Conv3D(480, 480),
            Conv3D(480, 240)
        )

        self.downsample = nn.MaxPool3d(kernel_size=2, stride=2)
        self.upsample = nn.Upsample(scale_factor=2, mode='trilinear')
        self.conv1 = Conv3D(240, 120)
        self.conv2 = Conv3D(120, 60)
        self.conv3 = Conv3D(60, 30)
        self.conv4 = Conv3D(30, 3, kernel=1, padding=0)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x1 = self.layer1(x)  #30, 128, 128, 128
        down1 = self.downsample(x1)  #30, 64, 64. 64

        x2 = self.layer2(down1)  #60, 64, 64, 64
        down2 = self.downsample(x2)  #60, 32, 32, 32

        x3 = self.layer3(down2)  #120, 32, 32, 32
        down3 = self.downsample(x3)  #120, 16, 16, 16

        x4 = self.layer4(down3)  #240, 16, 16, 16
        down4 = self.downsample(x4)  #240, 8, 8, 8

        x5 = self.layer5(down4)  #240-480-240, 240, 8, 8, 8
        up1 = self.upsample(x5)  #240, 16, 16, 16
        up1 = up1 + x4
        up1 = self.conv1(up1)  #120, 16, 16, 16

        up2 = self.upsample(up1)  #120, 32, 32, 32
        up2 = up2 + x3
        up2 = self.conv2(up2)  #60, 32, 32, 32

        up3 = self.upsample(up2)  #60, 64, 64, 64
        up3 = up3 + x2
        up3 = self.conv3(up3)  #30, 64, 64, 64

        up4 = self.upsample(up3)  #30, 128, 128, 128
        up4 = up4 + x1

        out = self.softmax(self.conv4(up4))  #3, 128, 128, 128

        return out



if __name__ == '__main__':
    x = t.randn((1, 4, 128, 128, 128))
    model = No_new_net()
    x = model(x)
    print(x.shape)