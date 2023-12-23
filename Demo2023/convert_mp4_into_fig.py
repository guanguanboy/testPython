from moviepy.editor import VideoFileClip

# 设置输入和输出文件路径
input_file = "input.mp4"  # 替换为你的输入视频文件路径
output_file = "output.gif"  # 替换为你的输出 GIF 文件路径

# 使用 VideoFileClip 加载视频文件
clip = VideoFileClip(input_file)

# 将视频转换为 GIF
clip.write_gif(output_file)

# 输出转换完成的消息
print("转换完成！")