import numpy as np
import cv2
import argparse
import datetime
import numpy as np
import time



ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

if args.get("video", None) is None:
    camera = cv2.VideoCapture('frame.avi')
else:
    camera = cv2.VideoCapture(args["video"])

(grabbed, frame) = camera.read()

fps = 30
height , width , layers =  frame.shape
codec = cv2.VideoWriter_fourcc('M','P','4','2')
videof  = cv2.VideoWriter('frame.avi',codec,fps,(width, height)) 

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100, # how many points
    qualityLevel = 0.1, #higher selects fewer points
    minDistance = 10, # higher selects fewer points, seen 2 and 5
    blockSize = 10 ) #  higher selects fewer points, seen 2 and 10:w

# Parameters for lucas kanade optical flow
lk_params = dict( 
     winSize  = (100,100),  #seen 10,10, seems larger can faster
     maxLevel = 10,   # seen 2 and 10
     criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))
 
# Take first frame and find corners in it
ret, old_frame = camera.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
 
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
 
while(1):
    ret,frame = camera.read()
    if ret != True:
	quit()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
# calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]
 
# draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)
 
    cv2.imshow('frame',img)    #lines
#    cv2.imshow('frame',frame) #just dots
    videof.write(frame)  #just dots
    videof.write(img)    #lines
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
# Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
 
videof.release()
cv2.destroyAllWindows()
camera.release()
