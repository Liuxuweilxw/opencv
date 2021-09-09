import cv2 as cv
import numpy as np


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate_demo", dst)


src = cv.imread("/Users/liuxuwei/Desktop/picture/templ.png")
cv.namedWindow("example", cv.WINDOW_FREERATIO)
cv.imshow("example", src)
# erode_demo(src)
dilate_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()