# import the necessary packages
from __future__ import print_function
import cv2
import argparse
import datetime
from matplotlib import pyplot as plt
import numpy as np
import time
 
 # construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picture", help="path to the picture file")
args = vars(ap.parse_args())
 
# load the image and convert it to grayscale
image = cv2.imread(args["picture"])
scale_factor = 0.1
height , width, layers  = image.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
image = cv2.resize(image, (width, height))
cv2.imshow('Original', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
  
# initialize the AKAZE descriptor, then detect keypoints and extract
# local invariant descriptors from the image
gray = np.float32(gray)  
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
image[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',image)
cv2.waitKey(0)
