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
filename = 'DJI_0023'
enhanced_filename = 'DJI_0023_result_Zero_DCE++'
low_light_imgs_path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/', filename)
enhanced_imgs_path = os.path.join('E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/', enhanced_filename)

import re

def extract_number(filename):
    # 使用正则表达式提取文件名中的数字部分
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return 0
    
# 获取图片文件夹中的所有文件
#image_files = sorted(os.listdir(low_light_imgs_path))
image_files = sorted(os.listdir(low_light_imgs_path), key=extract_number)
list_len = len(image_files)


# 设置目标宽度和高度为1080P
resized_width, resized_height = 1920, 1080

# 计算调整大小后的宽度和高度
target_width = resized_width*2
resized_height = resized_height

videoWriter = cv2.VideoWriter('videos/'+ filename + '_Zero_DCE_enhanced_fps60.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 60, (target_width,resized_height))

for  i in range(list_len):
    low_img  = cv2.imread(os.path.join(low_light_imgs_path, image_files[i])) 
    enh_img  = cv2.imread(os.path.join(enhanced_imgs_path, image_files[i])) 
    print(image_files[i])
    low_img_resized = cv2.resize(low_img,(resized_width,resized_height))
    enh_img_resized = cv2.resize(enh_img,(resized_width,resized_height))

    # 拼接图片
    combined_image = cv2.hconcat([low_img_resized, enh_img_resized])
    
    videoWriter.write(combined_image)