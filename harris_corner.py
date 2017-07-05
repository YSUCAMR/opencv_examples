import cv2
import numpy as np

filename = 'family.jpg'
img = cv2.imread(filename)
scale_factor = 0.2
height , width , layers = img.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
img = cv2.resize(img, (width, height))
cv2.imshow('Original', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

