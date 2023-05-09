import cv2
import numpy
import os
import glob as gb
import cv2
#filename = 'a0591'
#filename = 'a3629_1_5'
filename = 'a3629_last'
#filename = 'a0038'
#filename = 'a0093'


path = os.path.join('images/diffusion/', filename)

#path = 'images/harmoniaztion/generated_jpg_red_circle'
img_names_list = os.listdir(path)
list_len = len(img_names_list)

width = 1280
height = 960
videoWriter = cv2.VideoWriter('images/diffusion/video/'+ filename + '.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))

for  i in range(list_len):
    #img  = cv2.imread(os.path.join(path,str(999-i)+'.jpg'))
    if i > 50 and i % 6 != 0 and i < 950:
        continue
    img  = cv2.imread(os.path.join(path,img_names_list[list_len - i - 1]))
    img = cv2.resize(img,(width,height))
    videoWriter.write(img)

"""
def makevideo(path, fps):
    #将图片合成视频. path: 视频路径，fps: 帧率 
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    path1 = 'C:/Users/Administrator/Desktop/rocker1'   # 图像文件夹路径
    im = Image.open('C:/Users/Administrator/Desktop/rocker1/rocker1.jpg')  # 其中一张图像
    print(im.size)
    vw = cv2.VideoWriter(path, fourcc, fps, im.size)
    for i in os.listdir(path1):
        frame = cv2.imread(path1 + '/' + i)
        vw.write(frame)

if __name__ == '__main__':
    video_path = 'C:/Users/Administrator/Desktop/rocker.mp4'
    makevideo(video_path, 2)  # 图片转视频

"""