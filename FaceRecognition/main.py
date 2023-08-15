import cv2
import mediapipe as mp
import time

# cap=cv2.VideoCapture("../Chapters/res/video2.mp4")
cap=cv2.VideoCapture(0)

pTime=0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection=mpFaceDetection.FaceDetection(0.75) #min_detection_confidence=0.75, to remove false edges

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):
            #mpDraw.draw_detection(img, detection) #to automatically draw the box and facial feature points which detects the face.
            # print(f'id: {id}, detection: {detection}') #detection outputs: label_id:(face), score, location_data(relative_bounding_box[xmin,ymin, width, height], relative_keypoints[x,y]).
            # print(detection.score) #to get the score of detection class, which basically is the score which tells how likely the object is a face
            # print(detection.location_data.relative_bounding_box)

            #to draw the box manually:
            bboxC = detection.location_data.relative_bounding_box #bboxC: bounding box class
            ih, iw, ic = img.shape #to get the image height, width, channels
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih),\
                int(bboxC.width * iw), int(bboxC.height * ih) #\ to continue in next line, bbox: bounding box calculated
            cv2.rectangle(img,bbox,(255,0,255),2)

            #to display the confidence score on output screen
            cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                        (bbox[0], bbox[1]), cv2.FONT_HERSHEY_PLAIN,
                        2, (255, 0, 255), 2)

    #To calculate the FPS of the video, and display it
    cTime=time.time() #current time
    fps=1/(cTime-pTime)
    pTime=cTime #previous time
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_DUPLEX,3,(0,255,0),2)

    #Displaying the output
    cv2.namedWindow("video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("video", (900, 500))
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(1)