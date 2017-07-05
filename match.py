import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('family.jpg')
scale_factor = 0.3
height , width , layers = img_rgb.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
img_rgb = cv2.resize(img_rgb, (width, height))
cv2.imshow('Original', img_rgb)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('face.jpg',0)
scale_factor = 0.3
height , width = template.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
template = cv2.resize(template, (width, height))
cv2.imshow('template', template)
cv2.waitKey(0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('identified', img_rgb)
cv2.waitKey(0)

#for pt in zip(*loc[::-1]):
#    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#    cv2.imwrite('res.png',img_rgb)
