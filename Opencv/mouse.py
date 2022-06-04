import cv2
from cv2 import EVENT_RBUTTONDOWN
import numpy as np

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def clicking_event(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDOWN:
       print(x,',',y)
       
       font=cv2.FONT_HERSHEY_SIMPLEX
       strxy=str(x)+ ','+str(y)
       cv2.putText(img,strxy,font,1,(255,0,255),2)
       cv2.imshow('this',img)

img=np.zeros((600,600,3),np.uint8)   
cv2.imshow('this',img)

cv2.setMouseCallback('this',clicking_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
