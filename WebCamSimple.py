import cv2

capture = cv2.VideoCapture(0)
window = cv2.namedWindow("Video", 1)

while True:
  rval, frame = capture.read()
  if rval:
    # print frame.size().height
    cv2.imshow(window, frame)
  cv2.waitKey(20)
