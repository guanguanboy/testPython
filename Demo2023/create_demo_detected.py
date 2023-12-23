import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pickle

# 加载视频
video1 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/detection/DJI_0286_detected_yolov3.mp4')
video2 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/detection/DJI_0286_enhanced_detected_dino.mp4')

# 创建黑色背景图像
background_color = (0, 0, 0)  # 黑色背景
background_width = 1920
background_height = 1080
background_image = Image.new('RGB', (background_width, background_height), background_color)

# 创建字体
font_size = 40
font = ImageFont.truetype('arial.ttf', font_size)

# 创建视频写入对象
output_filename = './videos/DJI_0286_detection_yolo_dino_demo.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_filename, fourcc, 30.0, (background_width, background_height))

# 调整视频大小
resize_width = 800
resize_height = 600

#读取person count list
video1_person_list_path = './Demo2023/DJI_0286_detected_person_list_yolov3.pkl'

# 读取.pkl文件并获取保存的列表
with open(video1_person_list_path, 'rb') as file:
    video1_person_list = pickle.load(file)

video1_car_list_path = './Demo2023/DJI_0286_detected_car_list_yolov3.pkl'

# 读取.pkl文件并获取保存的列表
with open(video1_car_list_path, 'rb') as file:
    video1_car_list = pickle.load(file)

#读取car count list
video2_person_list_path = './Demo2023/DJI_0286_enhanced_detected_person_list_dino.pkl'

# 读取.pkl文件并获取保存的列表
with open(video2_person_list_path, 'rb') as file:
    video2_person_list = pickle.load(file)

video2_car_list_path = './Demo2023/DJI_0286_enhanced_detected_car_list_dino.pkl'

# 读取.pkl文件并获取保存的列表
with open(video2_car_list_path, 'rb') as file:
    video2_car_list = pickle.load(file)

car_gt_list = [49,48,48,35,22,28,27,36,42,43,35,40,42,59,70,72,71,72,72,72,72,71,70,68,64,63,62,61,60,60,56,52,52,50]
person_gt_list = [28,28,28,26,24,22,20,20,24,24,22,22,22,20,20,24,25,23,23,20,20,20,20,18,18,18,18,18,16,16,16,16,15,15]
count_index = 0

video_detected_result = f'Person Count: 2000, Car Count: 4000'
person_detected_result = 'Person Count: 2000,'

# 处理视频帧
while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    if not ret1 or not ret2:
        break

# 调整视频大小
    frame1 = cv2.resize(frame1, (resize_width, resize_height))
    frame2 = cv2.resize(frame2, (resize_width, resize_height))

    # 将帧转换为PIL图像
    pil_frame1 = Image.fromarray(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    pil_frame2 = Image.fromarray(cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB))

    # 计算视频居中位置
    x_offset = (background_width//2 - resize_width) // 2
    y_offset = (background_height - resize_height) // 2

    # 将视频帧嵌入黑色背景图像
    background_image = Image.new('RGB', (background_width, background_height), background_color)

    background_image.paste(pil_frame1, (x_offset, y_offset -30))
    background_image.paste(pil_frame2, (background_width // 2 + x_offset, y_offset -30))

    # 在黑色背景上添加视频名称标记
    draw = ImageDraw.Draw(background_image)
    #video1_name = 'Low-light'
    #video2_name = 'Enhanced'
    video1_name = 'Low-light Dectection Results'
    video2_name = 'Enhanced Dectection Results'
    #draw.text((10, 10), video1_name, font=font, fill=(255, 255, 255))
    #draw.text((background_width // 2 + 10, 10), video2_name, font=font, fill=(255, 255, 255))
    # 计算视频名称起始位置
    video1_name_width, video1_name_height = draw.textsize(video1_name, font=font)
    video2_name_width, video2_name_height = draw.textsize(video2_name, font=font)
    video1_name_x = x_offset + (resize_width - video1_name_width) // 2
    #video1_name_y = y_offset + resize_height + (background_height - resize_height - video1_name_height) // 2
    video1_name_y = (background_height - resize_height) // 4
    video2_name_x = background_width // 2 + x_offset + (resize_width - video2_name_width) // 2
    #video2_name_y = y_offset + resize_height + (background_height - resize_height - video2_name_height) // 2
    video2_name_y = (background_height - resize_height) // 4

    draw.text((video1_name_x, video1_name_y), video1_name, font=font, fill=(255, 255, 255))
    draw.text((video2_name_x, video2_name_y), video2_name, font=font, fill=(255, 255, 255))

    video1_car_count = video1_car_list[count_index]
    video1_person_count = video1_person_list[count_index]

    video1_detected_result = f"Person Count: {video1_person_count:<4}" + "\n" + f"Car Count: {video1_car_count:<4}"
    
    #确定绘制位置
    video1_detected_result_for_len = f"Person Count: 100" + "\n" + f"Car Count: 100"

    video1_detected_result_width, video1_detected_result_height = draw.textsize(video1_detected_result_for_len, font=font)

    video1_detected_result_x = x_offset + (resize_width - video1_detected_result_width) // 2
    video1_detected_result_y = (background_height - resize_height) // 2 + resize_height
    draw.text((video1_detected_result_x, video1_detected_result_y), video1_detected_result, font=font, fill=(255, 255, 255))
    
    video2_car_count = video2_car_list[count_index]
    video2_person_count = video2_person_list[count_index]
    #video2_detected_result = f"Person Count: {video2_person_count:<6}, Car Count: {video2_car_count:<6}"
    
    video2_detected_result = f"Person Count: {video2_person_count:<4}" + "\n" + f"Car Count: {video2_car_count:<4}"
    #确定绘制位置
    video2_detected_result_for_len = f"Person Count: 100" + "\n" + f"Car Count: 100"
    video2_detected_result_width, video2_detected_result_height = draw.textsize(video2_detected_result_for_len, font=font)
    video2_detected_result_x = background_width // 2 + x_offset + (resize_width - video2_detected_result_width) // 2
    video2_detected_result_y = (background_height - resize_height) // 2 + resize_height
    
    draw.text((video2_detected_result_x, video2_detected_result_y), video2_detected_result, font=font, fill=(255, 255, 255))

    person_count_gt = person_gt_list[count_index//30]
    cat_count_gt = car_gt_list[count_index//30]
    video1_detected_GT = f"Person Count GT: {person_count_gt}" + "\n" + f"Car Count GT: {cat_count_gt}"
    video1_detected_GT_for_len = f"Person Count GT: 100" + "\n" + f"Car Count GT: 100"
    video1_detected_GT_width, video1_detected_GT_height = draw.textsize(video1_detected_GT_for_len, font=font)
    video1_detected_GT_x = (background_width - video1_detected_GT_width) // 2
    video1_detected_GT_y = (background_height - resize_height) // 2 + resize_height
    draw.text((video1_detected_GT_x, video1_detected_GT_y), video1_detected_GT, font=font, fill=(0, 0, 255))
    # 将图像转换回OpenCV格式并写入输出视频
    output_frame = cv2.cvtColor(np.array(background_image), cv2.COLOR_RGB2BGR)
    output_video.write(output_frame)

    count_index = count_index + 1


    # 显示图像
    cv2.imshow('Embedded Videos', output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理资源
video1.release()
video2.release()
output_video.release()
cv2.destroyAllWindows()