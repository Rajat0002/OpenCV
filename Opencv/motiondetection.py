import cv2
import numpy as np

capture=cv2.VideoCapture(0)

ret, frame1=capture.read()
ret, frame2=capture.read()

while capture.isOpened():
    #ret, frame=capture.read()
    diff=cv2.absdiff(frame1,frame2)  
            #finding absolute difference between between first and second frame
    gray=cv2.cvtColor(diff,cv2.COLOR_BGRA2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)

        if cv2.contourArea(contour)>700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Status:{}".format('Mvement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.imshow('VIDEO',frame1)
    frame1=frame2
    ret,frame2=capture.read()
    if cv2.waitKey(40)==27:
        break

cv2.destroyAllWindows()
capture.release()    