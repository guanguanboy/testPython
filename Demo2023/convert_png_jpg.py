import os
from PIL import Image

# 原始文件夹路径
source_folder = 'E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/IDR_denoise_res/gaussian_n/sigma-25/'

# 目标文件夹路径
target_folder = 'E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/IDR_denoise_res/gaussian_n/sigma-25_jpg/'

# 创建目标文件夹（如果不存在）
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历原始文件夹中的所有文件
for file_name in os.listdir(source_folder):
    # 拼接原始文件的完整路径
    source_path = os.path.join(source_folder, file_name)

    # 检查文件是否为图片且包含 "out.png" 字符串
    if os.path.isfile(source_path) and file_name.lower().endswith('out.png'):
        # 使用下划线分割文件名
        parts = file_name.split('_')

        # 使用文件名的第一部分作为新文件的名称
        new_file_name = parts[0] + '.jpg'
        print(new_file_name)
        # 拼接目标文件的完整路径
        target_path = os.path.join(target_folder, new_file_name)

        # 打开原始图片
        image = Image.open(source_path)

        # 将图片保存为 JPG 格式
        image.save(target_path, 'JPEG')