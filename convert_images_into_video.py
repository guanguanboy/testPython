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
filename = 'DJI_0286'

path = os.path.join('images/result_RetinexNet/', filename)

img_names_list = os.listdir(path)
list_len = len(img_names_list)

width = 1920
height = 1080
videoWriter = cv2.VideoWriter('videos/'+ filename + '_RetinexNet_enhanced_fps60.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 60, (width,height))

for  i in range(list_len):
    img  = cv2.imread(os.path.join(path,str(i+1)+'_S.jpg')) 
    img = cv2.resize(img,(width,height))
    videoWriter.write(img)