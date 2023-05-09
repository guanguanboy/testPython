import os
from PIL import Image
import cv2, math
import numpy as np
import imageio

#源目录
myPath = './images/uav/'
#输出目录
outPath = './images/fog/'
#D:\Codes\PycharmProjects\TestPython\images\harmoniaztion\a0249\fog
def processImage(filesource, destsource, name, imgtype):
    '''
    filesource是存放待雾化图片的目录
    destsource是存放物化后图片的目录
    name是文件名
    imgtype是文件类型
    '''
    imgtype = 'jpeg' if imgtype == '.jpg' else 'png'
    #打开图片
    source_img = os.path.join(filesource, name)
    print(source_img)
    print(name)
    img = cv2.imread(source_img)
    img_f = img / 255.0
    (row, col, chs) = img.shape

    A = 0.6  # 亮度
    beta = 0.1  # 雾的浓度
    size = math.sqrt(max(row, col))  # 雾化尺寸
    center = (row // 2, col // 2)  # 雾化中心
    for j in range(row):
        for l in range(col):
            d = -0.04 * math.sqrt((j - center[0]) ** 2 + (l - center[1]) ** 2) + size
            td = math.exp(-beta * d)
            img_f[j][l][:] = img_f[j][l][:] * td + A * (1 - td)
    dest_image_name = destsource + name
    print('dest_image_name=', dest_image_name)
    print('name=', name)

    imageio.imsave(dest_image_name, np.array( img_f*255))
 
def run():
    #切换到源目录，遍历目录下所有图片
    if not os.path.exists(outPath):
        os.makedirs(outPath)

    for i in os.listdir(myPath):
        #检查后缀
        postfix = os.path.splitext(i)[1]
        print(postfix,i)
        if postfix == '.jpg' or postfix == '.png':
            processImage(myPath, outPath, i, postfix)
 
if __name__ == '__main__':
    run()
