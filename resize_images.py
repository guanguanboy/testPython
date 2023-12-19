from PIL import Image
import os

# 原始图片文件夹路径
source_folder = 'E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/DJI_0014_result_Zero_DCE++/'

# 目标文件夹路径
target_folder = 'E:/Datasets/DroneDatasets/SeeBelow/Captured0316/100MEDIA/DJI_0014_result_Zero_DCE++_resized/'

# 创建目标文件夹（如果不存在）
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 获取原始图片文件夹中的所有文件
image_files = os.listdir(source_folder)

# 遍历图片文件列表，将每张图片缩小为原来的一半尺寸，并保存到目标文件夹
for image_file in image_files:
    # 拼接原始图片文件路径
    source_path = os.path.join(source_folder, image_file)
    print(image_file)
    # 打开原始图片
    image = Image.open(source_path)

    # 获取原始图片的宽度和高度
    width, height = image.size

    # 计算缩小后的宽度和高度
    new_width = width // 2
    new_height = height // 2

    # 缩小图片尺寸
    resized_image = image.resize((new_width, new_height))

    # 拼接目标图片文件路径
    target_path = os.path.join(target_folder, image_file)

    # 保存缩小后的图片到目标文件夹
    resized_image.save(target_path)