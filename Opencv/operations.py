import cv2 as cv
import numpy as np

pic1=np.zeros((300,500,3),np.uint8)
pic1=cv.rectangle(pic1,(200,0),(300,100),(255,255,255),-1)
pic2=cv.imread('C:\\that.png')

bitAnd=cv.bitwise_or(pic2,pic1)
cv.imshow('IMAGE1',pic1)
cv.imshow('IMAGE2',pic2)
cv.imshow('IMAGE3',bitAnd)
cv.waitKey(0)
cv.destroyAllWindows()