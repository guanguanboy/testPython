import cv2
import numpy
import os
import glob as gb
import cv2
#filename = 'a0591'
#filename = 'a0867'
#filename = 'a0038'
#filename = 'a0093'
#filename = 'c462875'
#filename = 'a3074'
filename = 'DJI_0014'

#path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/Results/DJI_0014_jpg_result_SCI/')

#path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/DJI_0014_resized/')
#path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/DJI_0014_result_Zero_DCE++_resized/')
#path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/IDR_denoise_res/gaussian_n/sigma-25_jpg/')
path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/Results/RentinexNet/DJI_0014/')

import re

def extract_number(filename):
    # 使用正则表达式提取文件名中的数字部分
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return 0

image_files = sorted(os.listdir(path), key=extract_number)
list_len = len(image_files)

width = 1920
height = 1080
#videoWriter = cv2.VideoWriter('videos/'+ filename + '_SCI_enhanced_fps30.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
#videoWriter = cv2.VideoWriter('videos/'+ filename + '_resized_fps30.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
#videoWriter = cv2.VideoWriter('videos/'+ filename + '_DCE++_enhanced_fps30.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
#videoWriter = cv2.VideoWriter('videos/'+ filename + '_DCE++_enhanced_denoised_fps30.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
videoWriter = cv2.VideoWriter('videos/'+ filename + '_RetinexNet_enhanced_fps30.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))
for  i in range(list_len):
    img  = cv2.imread(os.path.join(path,str(i+1)+'_S.jpg')) 
    img = cv2.resize(img,(width,height))
    videoWriter.write(img)