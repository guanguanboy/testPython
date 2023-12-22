import cv2

# 打开视频文件
video_path = 'D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced_seged_by_mask2former_part_class.mp4'  # 替换为你的视频文件路径
cap = cv2.VideoCapture(video_path)

# 获取视频帧的宽度和高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建 VideoWriter 对象，用于保存输出视频
output_path = "D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced_seged_by_mask2former_part_class_with_rect.mp4"  # 替换为你想要保存的输出视频文件路径
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, 30.0, (frame_width, frame_height))



# 定义绿色框的位置和大小
box_x = 520  # 框的左上角 x 坐标
box_y = 330  # 框的左上角 y 坐标
box_width = 640  # 框的宽度
box_height = 480  # 框的高度

cropped_output_path = "D:/Codes/PycharmProjects/TestPython/videos/DJI_0286_enhanced_seged_by_mask2former_part_class_cropped.mp4"  # 替换为你想要保存的输出视频文件路径
croped_out = cv2.VideoWriter(cropped_output_path, fourcc, 30.0, (box_width, box_height))

# 处理视频的每一帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 裁剪绿色框内的内容
    cropped_frame = frame[box_y:box_y+box_height, box_x:box_x+box_width]
    
    # 将裁剪后的帧写入输出视频文件
    croped_out.write(cropped_frame)

    # 在帧上绘制绿色框
    cv2.rectangle(frame, (box_x, box_y), (box_x + box_width, box_y + box_height), (0, 255, 0), 2)

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