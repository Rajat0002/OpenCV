import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow("TRACKING")

capture=cv.VideoCapture(0)
cv.createTrackbar("LH","Tracking",0,255,nothing)
cv.createTrackbar("LS","Tracking",0,255,nothing)
cv.createTrackbar("LV","Tracking",0,255,nothing)
cv.createTrackbar("UH","Tracking",255,255,nothing)
cv.createTrackbar("US","Tracking",255,255,nothing)
cv.createTrackbar("UV","Tracking",255,255,nothing)





while True:
    #frame=cv.imread('C:\\balls.jpeg')
    _,frame=capture.read()
    cv.imshow('FRAME',frame)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_h=cv.getTrackbarPos("LH","Tracking")
    l_s=cv.getTrackbarPos("LS","Tracking")
    l_v=cv.getTrackbarPos("LV","Tracking")
    u_h=cv.getTrackbarPos("UH","Tracking")
    u_s=cv.getTrackbarPos("US","Tracking")
    key=cv.waitKey(1)
    if key==27:
       break
capture.release()
cv.destroyAllWindows()    