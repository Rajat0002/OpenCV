import cv2 as cv

img = cv.imread('C:\\thiss.jpg')

cv.imshow('Flower',img)
def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image= rescaleFrame(img)
cv.imshow('Flower',resized_image)

#work only for LIVE video
#def changeRes(width,height):
 #     capture.set(3,width)
  #    capture.set(4,width)
cv.waitKey(0)
