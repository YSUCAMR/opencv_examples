import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('juliet1.jpg')
cv2.imshow('Image1',im)
key = cv2.waitKey(3000)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image2',imgray)
key = cv2.waitKey(3000)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Image3',image)
key = cv2.waitKey(5000)
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow('Image4',img)
key = cv2.waitKey(5000)

