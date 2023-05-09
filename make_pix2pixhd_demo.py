import imageio
import os

path = 'images/pix2pixhd_imgs/generated_jpg_black_band'
img_names_list = os.listdir(path)
list_len = len(img_names_list)

gif_images = []
j=30
savepath = 'images/pix2pixhd_imgs/pix_gif'
for i in range(list_len):
    gif_images.append(imageio.imread(os.path.join(path,str(i)+'.jpg')))   # 读取多张图片
imageio.mimsave(os.path.join(savepath,'pix2pixHD_fps45.gif'), gif_images, fps=45)   # 转化为gif动画