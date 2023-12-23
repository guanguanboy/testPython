import os
import cv2

import re

# 图片文件夹路径
folder_path = "E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/Results/DJI_0014_SCI_enhanced_1024_768/"  # 替换为你的图片文件夹路径

output_folder_path = "E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/Results/DJI_0014_SCI_enhanced_1024_768_circled/"  # 替换为你的图片文件夹路径
if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)
# 定义圆圈的参数
circle1_center = (830, 260)  # 圆心坐标
circle1_radius = 120  # 圆的半径
circle_color = (0, 0, 255)  # 红色，BGR 格式
circle_thickness = 2  # 圆圈的线条粗细

circle2_center = (870, 510)  # 圆心坐标
circle2_radius = 120  # 圆的半径

circle3_center = (500, 450)  # 圆心坐标
circle3_radius = 200  # 圆的半径

def extract_number(filename):
    # 使用正则表达式提取文件名中的数字部分
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return 0

image_files = sorted(os.listdir(folder_path), key=extract_number)


# 遍历文件夹下的所有图片
index = 0
for filename in image_files:
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 读取图片
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        
        if index in range(0, 270):
            # 在图片上绘制红色圆圈
            cv2.circle(image, circle1_center, circle1_radius, circle_color, circle_thickness)
        
        if index in range(500, 740):
            # 在图片上绘制红色圆圈
            cv2.circle(image, circle2_center, circle2_radius, circle_color, circle_thickness)

        if index in range(800, 1020):
            # 在图片上绘制红色圆圈
            cv2.circle(image, circle3_center, circle3_radius, circle_color, circle_thickness)

        # 显示图片
        #cv2.imshow("Image", image)
        #cv2.waitKey(0)
        
        # 保存带有红色圆圈的图片
        output_path = os.path.join(output_folder_path + filename)
        cv2.imwrite(output_path, image)

        index = index+1
