import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('left2.png',0)
imgR = cv2.imread('right2.png',0)

cv2.imshow('Left side',imgL)
cv2.waitKey()

#stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
stereo = cv2.StereoBM_create( 16, 15)
disparity = stereo.compute(imgL,imgR)

plt.imshow(disparity,'gray')
plt.show()
