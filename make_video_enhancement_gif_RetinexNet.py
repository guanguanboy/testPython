import imageio
import os
import numpy as np
import cv2
from PIL import Image
from skimage.transform import resize

#filename = 'a0591'
#filename = 'a0093'
#filename = 'a0867'
filename = 'DJI_0286'
#filename = 'c462875'
#filename = 'a0249'
#rgb_img = imageio.imread('./images/harmoniaztion/a0093.jpg')
harmonization_root_path = './images/result_RetinexNet'
lowlight_img_paths = os.path.join(harmonization_root_path, filename)

img_names_list = os.listdir(lowlight_img_paths)
lowlight_list_len = len(img_names_list)

gif_images = []
"""
for i in range(epoch):
    split_width = 10*i
    if split_width < width_min:
        new_img[:,0:split_width,:] = rgb_img[:,0:split_width,:]
        new_img[:,split_width:,:] = seg_img[:,split_width:,:3]
    else:
        new_img = rgb_img

    img_name = str(i) + '.jpg'
    img_path = os.path.join(img_save_path, img_name)
    imageio.imsave(img_path, new_img)
"""
width = 640
height = 360

for i in range(lowlight_list_len):
    #if i % 2 != 0:
        #continue

    lowlight_img_path = os.path.join(lowlight_img_paths, str(i+1)+'_S.jpg')
    lowlight_img = imageio.imread(lowlight_img_path)
    print(lowlight_img.shape)
    #lowlight_img = cv2.resize(lowlight_img, (height, width),interpolation=cv2.INTER_CUBIC)
    lowlight_img = np.array(Image.fromarray(lowlight_img).resize((width,height)))
    #print(lowlight_img.shape)
    #cliped_img = lowlight_img[:,560:,:]

    gif_images.append(lowlight_img)


imageio.mimsave(os.path.join('./images/enhancement',filename + '_frame640_360P.gif'), gif_images, fps=30)   # 转化为gif动画
