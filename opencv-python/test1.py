import cv2 as cv
import numpy as np


def color_space(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yua",yuv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCR_CB)
    cv.imshow("Ycr_cb",Ycrcb)


src = cv.imread("C:/Users/liuxuwei/Desktop/2.jpg")
cv.namedWindow("input image")
cv.imshow("input image",src)
color_space(src)
cv.waitKey(0)

cv.destroyAllWindows()

