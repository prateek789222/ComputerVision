#Resize and crop image
import cv2

img = cv2.imread("res/img2.jpg")
print(img.shape) #o/p: (935, 1280, 3) (height, width, no. of channels)

imgResize = cv2.resize(img,(1000,500)) #(img,(width, height, no. of channels))
print(imgResize.shape) #o/p: (500, 1000, 3)

imgCropped = img[460:1190,352:895] #can be done without cv2. Specify start:end in [height,width] format

cv2.imshow("Image",img)
# cv2.imshow("Image Resized",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)