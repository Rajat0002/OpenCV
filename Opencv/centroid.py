import cv2 as cv
import numpy as np

img = np.zeros((500,600, 3), np.uint8)
  
# Three vertices(tuples) of the triangle 
p1 = (200, 400)
p2 = (100, 100)
p3 = (300, 100)
  

cv.line(img, p1, p2, (255, 0, 0), 3)
cv.line(img, p2, p3, (255, 0, 0), 3)
cv.line(img, p1, p3, (255, 0, 0), 3)
  

centroid = ((p1[0]+p2[0]+p3[0])//3, (p1[1]+p2[1]+p3[1])//3)
  
cv.circle(img, centroid, 4, (0, 255, 0))
  

cv.imshow("image", img)
cv.waitKey(0)