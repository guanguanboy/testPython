
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 加载视频
#video1 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286.MP4')
#video2 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced.mp4')
#video3 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286.MP4')
#video4 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced.mp4')

video1 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_seged_by_segformer_b0_with_rect.mp4')
video2 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced_seged_by_mask2former_part_class_with_rect.mp4')
video3 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_seged_by_segformer_b0_cropped.mp4')
#video4 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_DCE++_enhanced_denoised_fps30.mp4')
video4 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced_seged_by_mask2former_part_class_cropped.mp4')

# 创建黑色背景图像
background_color = (0, 0, 0)  # 黑色背景
background_width = 1920
background_height = 1080
background_image = Image.new('RGB', (background_width, background_height), background_color)

# 创建字体
font_size = 40
font = ImageFont.truetype('arial.ttf', font_size)

# 创建视频写入对象
output_filename = './videos/segmentation_video_4window.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_filename, fourcc, 30.0, (background_width, background_height))

# 调整视频大小
resize_width = 600
resize_height = 400

line1_point1 = (342,380)
line1_point2 = (180,540)

line2_point1 = (540,380)
line2_point2 = (780,540)

line3_point1 = (1300,380)
line3_point2 = (1140,540)

line4_point1 = (1500,380)
line4_point2 = (1740,540)

# 处理视频帧
while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    ret3, frame3 = video3.read()
    ret4, frame4 = video4.read()
    
    if not ret1 or not ret2:
        break

# 调整视频大小
    frame1 = cv2.resize(frame1, (resize_width, resize_height))
    frame2 = cv2.resize(frame2, (resize_width, resize_height))
    frame3 = cv2.resize(frame3, (resize_width, resize_height))
    frame4 = cv2.resize(frame4, (resize_width, resize_height))
    # 将帧转换为PIL图像
    pil_frame1 = Image.fromarray(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    pil_frame2 = Image.fromarray(cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB))
    pil_frame3 = Image.fromarray(cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB))
    pil_frame4 = Image.fromarray(cv2.cvtColor(frame4, cv2.COLOR_BGR2RGB))

    # 计算视频居中位置
    x_offset = (background_width//2 - resize_width)//2
    y_offset = (background_height//2 - resize_height)//2

    #x_offset = (background_width//2 - resize_width) // 2
    y_offset_below = background_height//2

    # 将视频帧嵌入黑色背景图像
    background_image.paste(pil_frame1, (x_offset, y_offset+10))
    background_image.paste(pil_frame2, (background_width // 2 + x_offset, y_offset+10))

    background_image.paste(pil_frame3, (x_offset, y_offset_below))
    background_image.paste(pil_frame4, (background_width // 2 + x_offset, y_offset_below))

    # 在黑色背景上添加视频名称标记
    draw = ImageDraw.Draw(background_image)
    video1_name = 'Low-light Segmentation Results'
    video2_name = 'Enhanced Segmentation Results'
    #draw.text((10, 10), video1_name, font=font, fill=(255, 255, 255))
    #draw.text((background_width // 2 + 10, 10), video2_name, font=font, fill=(255, 255, 255))
    video1_name_width, video1_name_height = draw.textsize(video1_name, font=font)
    video2_name_width, video2_name_height = draw.textsize(video2_name, font=font)
    video1_name_x = x_offset + (resize_width - video1_name_width) // 2
    #video1_name_y = y_offset + resize_height + (background_height - resize_height - video1_name_height) // 2
    video1_name_y = 10
    video2_name_x = background_width // 2 + x_offset + (resize_width - video2_name_width) // 2
    #video2_name_y = y_offset + resize_height + (background_height - resize_height - video2_name_height) // 2
    video2_name_y = 10

    draw.text((video1_name_x, video1_name_y), video1_name, font=font, fill=(255, 255, 255))
    draw.text((video2_name_x, video2_name_y), video2_name, font=font, fill=(255, 255, 255))

    draw.line([line1_point1, line1_point2], fill="green", width=5)
    draw.line([line2_point1, line2_point2], fill="green", width=5)
    draw.line([line3_point1, line3_point2], fill="green", width=5)
    draw.line([line4_point1, line4_point2], fill="green", width=5)

    # 将图像转换回OpenCV格式并写入输出视频
    output_frame = cv2.cvtColor(np.array(background_image), cv2.COLOR_RGB2BGR)
    output_video.write(output_frame)


    # 显示图像
    cv2.imshow('Embedded Videos', output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理资源
video1.release()
video2.release()
output_video.release()
cv2.destroyAllWindows()