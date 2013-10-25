import cv2

TRAINSET = "/Users/click/Codes/Arduino/lbpcascade_frontalface.xml"
DOWNSCALE = 4

webcam = cv2.VideoCapture(0)
window = cv2.namedWindow("preview", 1)
classifier = cv2.CascadeClassifier(TRAINSET)

while True:
  rval, frame = webcam.read()

  if rval:
    # detect faces and draw bounding boxes
    minisize = (frame.shape[1]/DOWNSCALE,frame.shape[0]/DOWNSCALE)
    miniframe = cv2.resize(frame, minisize)
    faces = classifier.detectMultiScale(miniframe)

    for f in faces:
      x, y, w, h = [ v*DOWNSCALE for v in f ]
      cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255))

    cv2.putText(frame, "Press ESC to close.", (5, 25),
          cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
    cv2.imshow(window, frame)

  if cv2.waitKey(20) == 27: # exit on ESC
    break
