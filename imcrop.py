from PIL import Image
import os

srcPath = './resize/origin/'   # 所要读取修改的文件夹
dstPath = './resize/target/'    # 修改后所存放路径
filelist = os.listdir(srcPath)

list1=[]
# 读取图片
for filename in filelist:
    filename1 = os.path.splitext(filename)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(filename)[0]  # 读取文件名
    list1.append(filename0+filename1)

for i in range(0,len(list1)):
    filea = str(srcPath+list1[i])
    img_1 = Image.open(filea)
    # 设置裁剪的位置
    crop_box = (550,250,1050,550)
    # 裁剪图片
    img_2 = img_1.crop(crop_box)
    #保存图片
    img_2.save(dstPath+list1[i])
print('已经截图成功')
