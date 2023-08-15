#face detection using opencv cascades
import cv2
import Stacking

faceCascade=cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")
img = cv2.imread("res/my.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

imgStack=Stacking.stackImages(0.2,([img]))
faces=faceCascade.detectMultiScale(imgGray,1.1,4)
cv2.imshow("Result", imgStack)
cv2.waitKey(0)