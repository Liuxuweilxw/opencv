import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,20,20)
    cv.imshow("shift_demo",dst)


src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
cv.imshow("example",src)
t1 = cv.getTickCount()
# bi_demo(src)
shift_demo(src)
t2 = cv.getTickCount()
print("%f 毫秒" % ((t2-t1)/cv.getTickFrequency()*1000))
cv.waitKey(0)
cv.destroyAllWindows()
