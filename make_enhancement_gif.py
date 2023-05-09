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
harmonization_root_path = './images/enhancement'
lowlight_img_paths = os.path.join(harmonization_root_path, filename)

enhanced_img_paths = os.path.join('images/result_RetinexNet/', filename)

img_names_list = os.listdir(lowlight_img_paths)
lowlight_list_len = len(img_names_list)

img_names_list = os.listdir(enhanced_img_paths)
enhanced_list_len = len(img_names_list)

assert lowlight_list_len == enhanced_list_len

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
frame_count=300
step = int(width/frame_count)

for i in range(frame_count):
    #if i % 2 != 0:
        #continue
    enhanced_img_path = os.path.join(enhanced_img_paths, str(i+1)+'_S.jpg')
    enhanced_img = imageio.imread(enhanced_img_path)
    print(type(enhanced_img), enhanced_img.shape)
    #enhanced_img = cv2.resize(enhanced_img, (height, width),interpolation=cv2.INTER_CUBIC)
    enhanced_img_resized = np.array(Image.fromarray(enhanced_img).resize((width, height)))
    print(enhanced_img_resized.shape)

    lowlight_img_path = os.path.join(lowlight_img_paths, str(i+1)+'.jpg')
    lowlight_img = imageio.imread(lowlight_img_path)
    #lowlight_img = cv2.resize(lowlight_img, (height, width),interpolation=cv2.INTER_CUBIC)
    lowlight_img = np.array(Image.fromarray(lowlight_img).resize((width,height)))
    print(lowlight_img.shape)
    new_img = np.full((height, width,  3), 255)
    split_width = 5+i*step
    if split_width + 5 < width:
        new_img[:,0:split_width,:] = enhanced_img_resized[:,0:split_width,:]
        new_img[:,split_width+5:,:] = lowlight_img[:,split_width+5:,:3]
    else:
        new_img = enhanced_img

    gif_images.append(new_img)


imageio.mimsave(os.path.join('./images/enhancement','DJI_0286_frame300_360P.gif'), gif_images, fps=30)   # 转化为gif动画
