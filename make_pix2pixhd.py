import imageio
import os
import numpy as np
rgb_img = imageio.imread('./images/pix2pixhd_imgs/teaser_ours.jpg')
print(rgb_img.shape)

seg_img = imageio.imread('./images/pix2pixhd_imgs/teaser_label.png')
print(seg_img.shape)

width_min = min(rgb_img.shape[1], seg_img.shape[1])
print(width_min)

new_img = np.zeros((1743, width_min, 3))
img_save_path = './images/pix2pixhd_imgs/generated/'
epoch = int(width_min/10 + 1)
for i in range(epoch):
    split_width = 10*i
    if split_width < width_min:
        new_img[:,0:split_width,:] = rgb_img[:,0:split_width,:]
        new_img[:,split_width:,:] = seg_img[:,split_width:,:3]
    else:
        new_img = rgb_img

    img_name = str(i) + '.png'
    img_path = os.path.join(img_save_path, img_name)
    imageio.imsave(img_path, new_img)