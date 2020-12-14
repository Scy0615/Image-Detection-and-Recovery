# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:39:58 2020

@author: Administrator
"""

import dlib
from imageio import imread, imsave
import numpy as np
import cv2
import imutils

def resize_crop_image(image,target_width,target_height):#裁剪图片
    (h, w) = image.shape[:2]
    dH =0
    dW=0
    if w < h:
        image = imutils.resize(image, width=target_width,
        inter=cv2.INTER_AREA)#基于区域像素关系的一种重采样或者插值方式
        dH = int((image.shape[0] - target_height) / 2.0)
    else:
        image = imutils.resize(image, height=target_height,
         inter=cv2.INTER_AREA)
        dW = int((image.shape[1] - target_width) / 2.0)
    (h, w) = image.shape[:2]
    image = image[dH:h - dH, dW:w - dW]
    return cv2.resize(image, (target_width, target_height),interpolation=cv2.INTER_AREA)

detector = dlib.get_frontal_face_detector()#检测人脸

path = "D:/study/项目/code/face/face_500.png"
print(imread(path).shape)
#for i in range(519, 550):
#    image_path = path + str(i) + ".png"
#    img = imread(image_path)
#    dets = detector(img)
#    for j, d in enumerate(dets):
#        bottom = d.bottom()
#        top = d.top()
#        left = d.left()
#        right = d.right()
#        if bottom > img.shape[0]:
#            bottom = img.shape[0]
#        if right > img.shape[1]:
#            right =  img.shape[1]
#        h = bottom - top
#        w = right - left
#        img_blank = np.zeros((h, w, 3), np.uint8)
#        for x in range(h):#裁剪人脸
#            for y in range(w):
#                img_blank[x][y] = img[top + x][left + y]
#        img_blank_1 = resize_crop_image(img_blank, 500, 500)
#        imsave("face_test/face_" + str(i) + ".png", img_blank_1)
#    print("finish%d"%i)

