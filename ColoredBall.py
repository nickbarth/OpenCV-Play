import cv2
import pdb
import numpy as np

capture = cv2.VideoCapture(0)
window = cv2.namedWindow("Video", 1)

while True:
  rval, frame = capture.read()
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
    lower_blue = np.array([200,80,40], np.uint8)
    upper_blue = np.array([230,110,60], np.uint8)
    ORANGE_MIN = np.array([5, 50, 50],np.uint8)
    ORANGE_MAX = np.array([15, 255, 255],np.uint8)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only blue colors
    frame = cv2.inRange(frame, ORANGE_MIN, ORANGE_MAX)

    ret,thresh = cv2.threshold(frame,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]

    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    # areas = [cv2.contourArea(c) for c in contours]

    """

    contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    largest_contour = None
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour=contour
            if not largest_contour==None:
                moment = cv2.moments(largest_contour)
                if moment["m00"] > 1000:
                    rect = cv2.minAreaRect(largest_contour)
                    rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
                    (width,height)=(rect[1][0],rect[1][1])
                    print width, height
                    box = cv2.cv.BoxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(frame, [box], 0, (255, 255, 255, 0), 2)
    """

    cv2.imshow(window, frame)
  cv2.waitKey(20)
  cv2.destroyAllWindows()

