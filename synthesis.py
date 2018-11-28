# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np


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
    mask = soft_mask < 1
    return mask


im = Image.open(r"imgs/download.jpg")
image = np.asarray(im)
h, w, c= np.shape(image)
print(c,h,w)
mask = gen_cir_mask(w, h)
print(mask)
image = mask.reshape(h, w, 1) * image
im = Image.fromarray(np.uint8(image))
plt.figure('abc')
plt.imshow(im)
plt.show()