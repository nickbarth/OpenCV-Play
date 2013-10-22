import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
window = cv2.namedWindow("preview", 1)

while True:
  rval, frame = webcam.read()

  if rval:
    frame = cv2.medianBlur(frame, 5)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(frame,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=5,maxRadius=50)
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),1) # draw the outer circle
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3) # draw the center of the circle

    cv2.imshow(window, frame)

  if cv2.waitKey(20) == 27:
    break
