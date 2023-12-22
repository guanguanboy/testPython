import cv2

# 打开视频文件
video1 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_DJI_0014_resized_fps30.mp4')
video2 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_RetinexNet_enhanced_fps30.mp4')
video3 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_SCI_enhanced_fps30.mp4')
#video4 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_DCE++_enhanced_denoised_fps30.mp4')
video4 = cv2.VideoCapture('D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_DJI_0014_DCE++_enhanced_fps30.mp4')

video_path = "DJI_0014_DJI_0014_resized_fps30.mp4"  # 替换为你的视频文件路径
cap = video1

# 获取视频帧的宽度和高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建 VideoWriter 对象，用于保存输出视频
output_path = "D:/Codes/PycharmProjects/TestPython/videos/DJI_0014_DJI_0014_resized_fps30_with_circle.mp4"  # 替换为你想要保存的输出视频文件路径
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, 30.0, (frame_width, frame_height))

# 定义圆圈的参数
circle_center = (300, 300)  # 圆心坐标
circle_radius = 100  # 圆的半径
circle_color = (0, 0, 255)  # 红色，BGR 格式
circle_thickness = 2  # 圆圈的线条粗细

# 处理视频的每一帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 在帧上绘制红色圆圈
    cv2.circle(frame, circle_center, circle_radius, circle_color, circle_thickness)
    
    # 显示帧
    cv2.imshow("Frame", frame)
    out.write(frame)
    
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()