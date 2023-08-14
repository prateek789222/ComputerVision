#Drawing shapes and adding text
import cv2
import numpy as np

img=np.zeros((420,420,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#cv2.shape_name(image,(from),(to),(color),width)

cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #cv2.FILLED-> fills the entire shape
cv2.circle(img,(400,300),60,(255,0,0),3)
cv2.putText(img,"PRATEEK",(100,200),cv2.FONT_HERSHEY_SIMPLEX,1.5,(200,200,200),5)

cv2.imshow("image",img)
cv2.waitKey(0)