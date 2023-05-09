import imageio
import os

filename = 'c462875'
path = 'images/harmoniaztion/generated_c462875'
#path = os.path.join('images/harmoniaztion/', 'generated_' + filename)
img_names_list = os.listdir(path)
list_len = len(img_names_list)

gif_images = []
j=30
savepath = 'images/harmoniaztion/pix_gif'
for i in range(list_len):
    gif_images.append(imageio.imread(os.path.join(path,str(i)+'.jpg')))   # 读取多张图片
imageio.mimsave(os.path.join(savepath,'harmonization_circle.gif'), gif_images, fps=60)   # 转化为gif动画