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
  
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(image,(x,y),3,255,-1)

plt.imshow(image),plt.show()
# draw the keypoints and show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
