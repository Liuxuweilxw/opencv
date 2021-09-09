import cv2 as cv
import numpy as np


def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("open_demo", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open_result", dst)


def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("close_demo", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close_result", dst)


src = cv.imread("/Users/liuxuwei/Desktop/picture/ellipses.jpg")
cv.namedWindow("example", cv.WINDOW_FREERATIO)
cv.imshow("example", src)
open_demo(src)
close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()