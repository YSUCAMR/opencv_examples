import numpy as np
import argparse
import cv2


image = cv2.imread('red_filament2.jpg')
scale_factor = 0.5

height , width , layers = image.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
#print width, height, dim
image = cv2.resize(image, (width, height))
#cv2.imshow('image', image)
#cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower1 = np.array([0, 150, 150])
upper1 = np.array([5, 255, 255])
lower2 = np.array([170, 150, 150])
upper2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
red1 = cv2.bitwise_and(image, image, mask=mask1)
red2 = cv2.bitwise_and(image, image, mask=mask2)
red  = cv2.addWeighted(red1, 1, red2, 1, 0)

red = cv2.medianBlur(red, 3)

gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
#gray = cv2.dilate(gray, None, iterations=1)

edged = cv2.Canny(gray, 100, 200)
#edged = cv2.dilate(edged, None, iterations=1)
#cv2.imshow('Edged', edged)
#cv2.waitKey(0)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
#closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
#cv2.imshow("Closed", edged)
#cv2.waitKey(0)
 
first_column = 0
second_column = 0
stats = []
for row in range(height):
    for column in range(width):
#	print edged[row,column] 
        if edged[row,column] > 128:
  	    if(first_column == 0):
                first_column = column
  	    elif(second_column == 0):
                second_column = column
	        distance = second_column - first_column
		stats.append(distance)
    first_column = 0
    second_column = 0
highest = 0
lowest = 1000
total = 0
index = 0
for item in stats:
    if item < lowest: 
        lowest = item
    if item > highest:
        highest = item
    total = total + item
    index = index + 1
average = total / index
print "average diameter = " + str(average)
print "max diameter = " + str(highest)
print "min diameter = " + str(lowest)

cv2.destroyAllWindows()


