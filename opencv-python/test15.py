import cv2 as cv
import numpy as np


def detect_circles_demo(image):
    cv.pyrMeanShiftFiltering(image, 10,100)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("circles", image)


src = cv.imread("C:/Users/liuxuwei/Desktop/smarties.png")
cv.namedWindow("example",cv.WINDOW_FREERATIO)
cv.imshow("example",src)
detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()