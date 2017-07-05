import cv2
import numpy as np
import argparse
import sys

print sys.argv[1]
image = cv2.imread(sys.argv[1])
scale_factor = 0.3

height , width , layers = image.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
print "resized" + str(height) + " " + str(width)
#print width, height, dim
image = cv2.resize(image, (width, height))
cv2.imshow('Original', image)
cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV', hsv)
#cv2.waitKey(0)

lower = np.array([90, 30, 30])
upper = np.array([150, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
blue = cv2.bitwise_and(image, image, mask=mask)
#blue = cv2.medianBlur(blue, 5)
cv2.imshow('Blue', blue)
cv2.waitKey(0)

gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
#gray = cv2.dilate(gray, None, iterations=1)
cv2.imshow('Dilated gray', gray)
cv2.waitKey(0)

edged = cv2.Canny(gray, 100, 200)
#edged = cv2.dilate(edged, None, iterations=1)
cv2.imshow('Edged', edged)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)
 
(img, cnts, hierarchy) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

index = 0
for c in cnts:
    peri = cv2.arcLength(c, True)
    print peri 
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    print approx
    cnt = cnts[index]
    cv2.drawContours(image, [cnt], 0, (0, 0, 255), 2)
    cv2.imshow("Output", image)
    print "object found " + str(index)
    cv2.waitKey(0)
    index += 1


cv2.destroyAllWindows()


