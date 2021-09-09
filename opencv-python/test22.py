import cv2 as cv
import numpy as np
import test13


def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("../opencv-master/data/lbpcascades/lbpcascade_frontalface_improved.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 3)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", image)


capture = cv.VideoCapture(0)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    # face_detect_demo(frame)
    test13.edge_demo(frame)
    c = cv.waitKey(10)
    if c == 27:
        break

cv.waitKey(0)
cv.destroyAllWindows()