import cv2
import numpy as np
import serial

PORT = '/dev/tty.usbserial-A1014R97'
SPEED = 9600

capture = cv2.VideoCapture(0)
window = cv2.namedWindow("Video", 1)

def send_int(val):
  connection = serial.Serial(PORT, SPEED, timeout=0, stopbits=serial.STOPBITS_ONE)
  connection.write(val)
  connection.flush()
  connection.close()

while True:
  rval, frame = capture.read()
  if rval:
    frame = cv2.medianBlur(frame, 5)
    frame = cv2.flip(frame, 1)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    BLUE_MIN = (90, 200, 100)
    BLUE_MAX = (110, 250, 255)
    frame = cv2.inRange(frame, BLUE_MIN, BLUE_MAX)
    # frame = cv2.Canny(frame, 0, 0, 0);
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(contour) for contour in contours]
    area = 0

    if areas:
      max_index = np.argmax(areas)
      biggest_contour = contours[max_index]
      area = cv2.contourArea(biggest_contour)

    if area > 10:
      x, y, w, h = cv2.boundingRect(biggest_contour)
      cv2.rectangle(frame, (x, y), (x+w, y+h), (179, 255, 255), 2)

      height, width = frame.shape
      # print x, y, height, width
      speed = (x * 100 / width) * 20 / 100
      speed = 80 + speed
      print speed
      send_int(chr(speed))

    cv2.imshow(window, frame)

  if cv2.waitKey(50) == 27:
    break

cv2.destroyAllWindows()
