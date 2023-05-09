import imageio
import os

path = 'images/test_images'
gif_images = []
j=30
savepath = 'images/gif'
for i in range(20):
    gif_images.append(imageio.imread(os.path.join(path,str(i)+'.jpg')))   # 读取多张图片
imageio.mimsave(os.path.join(savepath,'hello.gif'), gif_images, fps=5)   # 转化为gif动画