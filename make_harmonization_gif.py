import imageio
import os
import numpy as np
import cv2
from PIL import Image

#filename = 'a0591'
#filename = 'a0093'
#filename = 'a0867'
filename = 'a0237'
#filename = 'c462875'
#filename = 'a0249'
#rgb_img = imageio.imread('./images/harmoniaztion/a0093.jpg')
harmonization_root_path = './images/harmoniaztion'
imgs_path = os.path.join(harmonization_root_path, filename)

label_img_path = os.path.join(imgs_path, filename+'_text.jpg')
label_img = imageio.imread(label_img_path)

print(label_img.shape)

#seg_img = imageio.imread('./images/harmoniaztion/a0093_1_3.jpg')
composite_img_path = os.path.join(imgs_path, filename+'_1_3_text.jpg')
composite_img = imageio.imread(composite_img_path)
print(composite_img.shape)

width_min = min(label_img.shape[1], composite_img.shape[1])
print(width_min)

new_img = np.zeros((label_img.shape[0], width_min, 3))
img_save_path = './images/harmoniaztion/generated_' + filename + '/'
if not os.path.exists(img_save_path):
    os.mkdir(img_save_path)

epoch = int(width_min/10 + 1)

composite_img_path = os.path.join(imgs_path, filename+'_1.png')
mask = cv2.imread(composite_img_path, 0)

print(mask)
color=(255, 0, 0)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
print(contours)
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
for i in range(epoch):
    new_img = np.zeros((label_img.shape[0], width_min, 3))
    split_width = 10*i
    if split_width + 10 < width_min:
        new_img[:,0:split_width,:] = label_img[:,0:split_width,:]
        new_img[:,split_width+10:,:] = composite_img[:,split_width+10:,:3]
    else:
        new_img = label_img

    #new_img = np.int8(new_img)
    img = cv2.merge([new_img[:,:,0], new_img[:,:,1], new_img[:,:,2]])
    #image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.drawContours(img, contours, -1, color, 4)
    #new_img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

    img_name = str(i) + '.jpg'
    img_path = os.path.join(img_save_path, img_name)
    imageio.imsave(img_path, np.array(img))