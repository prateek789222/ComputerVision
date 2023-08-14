#Warp perspective
import cv2
import numpy as np

img = cv2.imread("res/img3.png")

height,width = 480,1120 #specify the h,w of the extracted object from the image

pts1 = np.float32([[208,322],[1388,414],[211,540],[1348,697]]) #Specify 4 points for the object to be extracted

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #specify the
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)