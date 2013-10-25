import cv2
import cv
# import pdb
import numpy as np

capture = cv2.VideoCapture(0)
window = cv2.namedWindow("Video", cv2.CV_WINDOW_AUTOSIZE)

def mouseEvent(event, x, y, flags, param):
  print event
  # jif event == cv2.CV_EVENT_LBUTTONDOWN:
  # print "x: ", x, ", y:", y


while True:
  rval, frame = capture.read()
  def mouseEvent(event, x, y, flags, param):
    print event
  cv2.setMouseCallback("Video", mouseEvent, None)
  if rval:
    frame = cv2.medianBlur(frame, 5)
    frame = cv2.flip(frame, 1)

    # pdb.set_trace()
    # R G B = B G R
    # frame = cv2.inRange(frame, (0, 20, 190, 0), (80, 240, 230, 0))
    # separated = cv2.inRange(frame, (255, 255, 255, 0), (255, 255, 255, 0))
    # frame = cv2.Canny(frame, 50, 200, 3);
    # frame = cv2.inRange(frame, (0, 0, 10, 0), (255, 255, 250, 0))
    # define range of blue color in HSV
    # lower_blue = np.array([200,80,40], np.uint8)
    # upper_blue = np.array([230,110,60], np.uint8)
    # ORANGE_MIN = np.array([5, 50, 50],np.uint8)
    # ORANGE_MAX = np.array([15, 255, 255],np.uint8)

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # frame = cv2.inRange(frame, (60, 50, 80, 0), (100, 100, 100, 0))

    # Threshold the HSV image to get only blue colors
    # frame = cv2.inRange(frame, ORANGE_MIN, ORANGE_MAX)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # frame = cv2.inRange(frame, BLUE_MIN, BLUE_MAX)
    # frame = cv2.inRange(frame, (50, 0, 0, 0), (220, 120, 120, 0))

    # ret,thresh = cv2.threshold(frame,127,255,0)
    # contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # areas = [cv2.contourArea(c) for c in contours]
    # max_index = np.argmax(areas)
    # cnt = contours[max_index]

    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    # frame = cv2.Canny(frame, 0, 30, 3);

    cv2.imshow(window, frame)

  if cv2.waitKey(20) == 27:
    break

cv2.destroyAllWindows()

