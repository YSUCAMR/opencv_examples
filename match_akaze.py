# import the necessary packages
from __future__ import print_function
import cv2
import argparse
import datetime
import numpy as np
import time
 
 # construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p1", "--picture1", help="path to the picture file")
ap.add_argument("-p2", "--picture2", help="path to the picture file")
args = vars(ap.parse_args())
 
# load the image and convert it to grayscale
img1 = cv2.imread(args["picture1"])
img2 = cv2.imread(args["picture2"])
scale_factor = 0.2
height , width, layers  = img1.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
img1 = cv2.resize(img1, (width, height))
img2 = cv2.resize(img2, (width, height))
cv2.imshow('Original 1', img1)
cv2.waitKey(0)
cv2.imshow('Original 2', img2)
cv2.waitKey(0)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
  
# initialize the AKAZE descriptor, then detect keypoints and extract
# local invariant descriptors from the image
detector = cv2.AKAZE_create()
(kp1, des1) = detector.detectAndCompute(gray1, None)
(kp2, des2) = detector.detectAndCompute(gray2, None)
print("keypoints: {}, descriptors: {}".format(len(kp1), des1.shape))
print("keypoints: {}, descriptors: {}".format(len(kp2), des2.shape))
   
# draw the keypoints and show the output image
cv2.drawKeypoints(img1, kp1, img1, (0, 255, 0))
cv2.drawKeypoints(img2, kp2, img2, (0, 255, 0))
cv2.imshow("Output1", img1)
cv2.waitKey(0)
cv2.imshow("Output2", img2)
cv2.waitKey(0)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)
cv2.imshow("final", img3)
cv2.waitKey(0)




