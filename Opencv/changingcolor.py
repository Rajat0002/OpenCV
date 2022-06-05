from attr import NOTHING
import cv2 as cv
from cv2 import ellipse
import numpy as np

def NOTHING(x):
    print(x)
image=np.zeros((300,500,3),np.uint8)
cv.namedWindow('PICTURE')

cv.createTrackbar('B','PICTURE',0,255,NOTHING)
cv.createTrackbar('G','PICTURE',0,255,NOTHING)
cv.createTrackbar('R','PICTURE',0,255,NOTHING)

switch='0: OFF\n 1:ON'
cv.createTrackbar(switch,'PICTURE',0,1,NOTHING)  

while(1):
    cv.imshow('PICTURE',image)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    b=cv.getTrackbarPos('B','PICTURE')
    g=cv.getTrackbarPos('G','PICTURE')
    r=cv.getTrackbarPos('R','PICTURE')
    s=cv.getTrackbarPos(switch,'PICTURE')

    if s==0:
        image[:]=0
    else:
        image[:]=[b,g,r]

cv.destroyAllWindows()    