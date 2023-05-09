import cv2
import imageio
from imgaug import augmenters as iaa #引入数据增强的包

seq = iaa.Sequential([         #建立一个名为seq的实例，定义增强方法，用于增强
    #iaa.Crop(px=(0, 16)),     #对图像进行crop操作，随机在距离边缘的0到16像素中选择crop范围
    #iaa.Fliplr(0.5),     #对百分之五十的图像进行做左右翻转
    iaa.GaussianBlur(sigma=2.8)     #在模型上使用0均值1方差进行高斯模糊
])

"""
seq = iaa.Sequential([
    # 选择2到3种方法做变换
    iaa.SomeOf((2, 3),
               [
                   iaa.imgcorruptlike.MotionBlur(severity=(1, 2)),  # 运动模糊
                   # iaa.Clouds(),  # 云雾
                   iaa.imgcorruptlike.Fog(severity=1),  # 多雾/霜
                   # iaa.imgcorruptlike.Snow(severity=2),  # 下雨、大雪
                   iaa.Rain(drop_size=(0.10, 0.15), speed=(0.1, 0.2)),  # 雨
                   iaa.Snowflakes(flake_size=(0.1, 0.4), speed=(0.01, 0.03)), # 雪点
                   # iaa.FastSnowyLandscape(lightness_threshold=(100, 255),lightness_multiplier=(1.5, 2.0)), # 雪地   亮度阈值是从 uniform(100, 255)（每张图像）和来自 uniform(1.5, 2.0)（每张图像）的乘数采样的。 这似乎产生了良好而多样的结果。
                   # iaa.imgcorruptlike.Spatter(severity=5),  # 溅 123水滴、45泥

                   # 对比度 亮度 饱和度 选其一
                   iaa.SomeOf((1, 1),
                       [
                           iaa.imgaug.augmenters.contrast.LinearContrast((0.5, 2.0), per_channel=0.5),  # 对比度变为原来的一半或者二倍
                           iaa.imgcorruptlike.Brightness(severity=(1, 2)),  # 亮度增加
                           iaa.imgcorruptlike.Saturate(severity=(1, 3)),  # 色彩饱和度
                       ]
                   )
               ],
               # 随机顺序运行augmentations
               random_order=True
               )
], random_order=True)  # 随机运行augmenters数量
"""

img = cv2.imread('./images/harmoniaztion/a0093/a0093_1_5.jpg')

images_aug = seq.augment_image(img)    #应用数据增强

cv2.imwrite('./images/harmoniaztion/a0093/a0093_1_5_blured.jpg',images_aug)
#imageio.imsave('./images/harmoniaztion/a0093/a0093_1_5_blured.jpg',images_aug)


img_ret3 = cv2.GaussianBlur(img,(57,57),0)
cv2.imwrite('./images/harmoniaztion/a0093/a0093_1_5_blured_opencv.jpg',img_ret3)


print(images_aug.shape)

print(type(images_aug))
