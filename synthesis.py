# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import cv2


# im = Image.open(r"imgs/background.jpg")
# draw = ImageDraw.Draw(im)
# myfont = ImageFont.truetype(u"D:\\ASE\\Poetic-Image\\imgs\\font1556\\handwriting.ttf", size=35)
# fillcolor = 'black'
# draw.text((350, 400), u"还有谁！！", font=myfont, fill=fillcolor)
# plt.figure('abc')
# plt.imshow(im)
# plt.show()

def gen_cir_mask(w, h):
    m_x, m_y = np.meshgrid(np.arange(w), np.arange(h))
    c_x = (w-1) / 2.0
    c_y = (h-1) / 2.0
    soft_mask = (m_x - c_x) ** 2 / (c_x ** 2) + (m_y - c_y) ** 2 / (c_y ** 2)
    Z = np.where(soft_mask<0.95, np.ones_like(soft_mask), np.zeros_like(soft_mask))
    Z_2 = np.where(abs(soft_mask-0.975)<0.025, np.ones_like(soft_mask), np.zeros_like(soft_mask))
    #Z_2 = np.where((1-soft_mask)<0.05, np.ones_like(soft_mask), np.zeros_like(soft_mask))
    return Z, Z_2

im = Image.open(r"imgs/download.jpg")
image = np.asarray(im)
h, w, c= np.shape(image)
width, height = im.size


bg_img_2 =  Image.open("./bg.jpg") # background image
bg_img_2_resized = bg_img_2.resize((800,600), Image.ANTIALIAS)
bg_crop= np.asarray(np.asarray(bg_img_2_resized))[0:height, 0:width,:]

mask,mask_2 = gen_cir_mask(w, h)
mask =  np.transpose(np.repeat(np.expand_dims(mask,0), 3, axis=0), (1,2,0))
mask_2 =  np.transpose(np.repeat(np.expand_dims(mask_2,0), 3, axis=0), (1,2,0))

#word_font = ImageFont.truetype("arial.ttf", 40)
word_font = ImageFont.truetype(u"./handwriting.ttf", size=35)


# generate mask
image = np.asarray(im)
image_2 = np.where(mask==1, image,bg_crop)
image_2 = np.where(mask_2==1, 0, image_2)


im_2 = Image.fromarray(np.uint8(image_2))
im_resized = im_2.resize((500,300), Image.ANTIALIAS)
pic_height, pic_width,_ = np.shape(im_resized)
bg_height, bg_width,_ = np.shape(bg_img_2_resized)
top_left_h = int(bg_height*0.7/2-pic_height/2)
topp_left_w = int(bg_width/2 - pic_width/2)
bg_img_2_resized.paste(im_resized, (topp_left_w,top_left_h))


draw_whole = ImageDraw.Draw(bg_img_2_resized)
draw_whole.text((300, 400),"Sample Text 1",(0,0,0),font=word_font)
draw_whole.text((300, 500),"Sample Text 1",(0,0,0),font=word_font)
plt.imshow(bg_img_2_resized)

bg_img_2_resized.save('./output.jpeg', 'jpeg')
plt.show()
