import torch as t
import torch.nn as nn
import numpy as np

class Conv3D(nn.Module):
    def __init__(self, c, o, kernel=3, stride=1, padding=1, g=1):
        super(Conv3D, self).__init__()
        if padding == None:
            padding = (kernel - 1) // 2
        self.conv = nn.Conv3d(c, o, kernel_size=kernel, stride=stride, padding=padding, groups=g, )
        self.bn = nn.BatchNorm3d(o)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        h = self.conv(x)
        h = self.bn(h)
        h = self.relu(h)

        return h


class Unet_3D(nn.Module):
    def __init__(self, f=16):
        super(Unet_3D, self).__init__()

        self.layer1 = nn.Sequential(
            Conv3D(4, f)
        )

        self.layer2 = nn.Sequential(
            Conv3D(f, 2*f),
            Conv3D(2*f, 2*f)
        )

        self.layer3 = nn.Sequential(
            Conv3D(2*f, 4*f),
            Conv3D(4*f, 4*f),
            Conv3D(4*f, 4*f)
        )

        self.layer4 = nn.Sequential(
            Conv3D(4*f, 8*f),
            Conv3D(8*f, 8*f),
            Conv3D(8*f, 8*f)
        )

        self.layer5 = nn.Sequential(
            Conv3D(8*f, 16*f),
            Conv3D(16*f, 16*f),
            Conv3D(16*f, 16*f)
        )

        self.downsample = nn.MaxPool3d(kernel_size=2, stride=2)

        self.upsample11 = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='trilinear'),
            Conv3D(16*f, 8*f)
        )

        self.upsample12 = nn.Sequential(
            Conv3D(16 * f, 8 * f),
            Conv3D(8 * f, 8 * f),
            Conv3D(8 * f, 8 * f)
        )

        self.upsample21 = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='trilinear'),
            Conv3D(8*f, 4*f)
        )

        self.upsample22 = nn.Sequential(
            Conv3D(8 * f, 4 * f),
            Conv3D(4 * f, 4 * f),
            Conv3D(4 * f, 4 * f)
        )

        self.upsample31 = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='trilinear'),
            Conv3D(4 * f, 2 * f)
        )

        self.upsample32 = nn.Sequential(
            Conv3D(4 * f, 2 * f),
            Conv3D(2 * f, 2 * f),
            Conv3D(2 * f, 2 * f)
        )

        self.upsample41 = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='trilinear'),
            Conv3D(2 * f, f)
        )

        self.upsample42 = nn.Sequential(
            Conv3D(2 * f, f),
            Conv3D(f, f),
            Conv3D(f, 3)
        )


        self.conv = Conv3D(3, 1, kernel=1, padding=0)
        self.softmax = nn.Softmax(dim=1)
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout3d(p=0.5)

    def forward(self, x):
        x1 = self.layer1(x)  #16, 128, 128, 128
        down1 = self.downsample(x1)  #16, 64, 64. 64

        x2 = self.layer2(down1)  #32, 64, 64, 64
        down2 = self.downsample(x2)  #32, 32, 32, 32

        x3 = self.layer3(down2)  #64, 32, 32, 32
        down3 = self.downsample(x3)  #64, 16, 16, 16

        x4 = self.layer4(down3)  #128, 16, 16, 16
        x4 = self.dropout(x4)
        down4 = self.downsample(x4)  #128, 8, 8, 8

        x5 = self.layer5(down4) #256, 8, 8, 8
        x5 = self.dropout(x5)

        up1 = self.upsample11(x5)  #128, 16, 16, 16
        up1 = t.cat([x4, up1], dim=1)
        up1 = self.upsample12(up1)  #128, 16, 16, 16

        up2 = self.upsample21(up1)  #64, 32, 32, 32
        up2 = t.cat([x3, up2], dim=1)
        up2 = self.upsample22(up2)  #64, 32, 32, 32

        up3 = self.upsample31(up2)  #32, 64, 64, 64
        up3 = t.cat([x2, up3], dim=1)
        up3 = self.upsample32(up3)  #32, 64, 64, 64



        up4 = self.upsample41(up3)  #16, 128, 128, 128
        up4 = t.cat([x1, up4], dim=1)
        up4 = self.upsample42(up4)  #3, 128, 128, 128

        out = self.sigmoid(self.conv(up4))  #1, 128, 128, 128

        return out


if __name__ == '__main__':
    x = t.randn((1, 4, 128, 128, 128))
    model = Unet_3D()
    x = model(x)
    print(x.shape)