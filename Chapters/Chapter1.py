import cv2
print("package imported")

# to capture image:
# img = cv2.imread("res/img1.jpg")
# cv2.imshow("output",img)
# cv2.waitKey(0)

# to capture video:
# cap=cv2.VideoCapture("res/video1.mp4")
# while True:
#     success,vid=cap.read()
#     cv2.imshow("Video",vid)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# to capture from webcam:
webcap=cv2.VideoCapture(0)
webcap.set(3,640) # id 3:width, 4:height
webcap.set(4,480)
webcap.set(10,100) #id 10: brightness
while True:
    success,web=webcap.read()
    cv2.imshow("Video",web)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break