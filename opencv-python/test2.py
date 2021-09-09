import cv2 as cv
import numpy as np


def add_demo(s1,s2):
    dst = cv.add(s1,s2)
    cv.imshow("add_demo",dst)


def subtract_demo(s1,s2):
    dst = cv.subtract(s1,s2)
    cv.imshow("substract_demo",dst)


def divide_demo(s1,s2):
    dst = cv.divide(s1,s1)
    cv.imshow("divide_demo",dst)


def mul_demo(s1,s2):
    dst = cv.multiply(s1,s2)
    cv.imshow("multiply",dst)


def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("contrast_brightness_demo",dst)


src1 = cv.imread("C:/Users/liuxuwei/Desktop/LinuxLogo.jpg")
src2 = cv.imread("C:/Users/liuxuwei/Desktop/WindowsLogo.jpg")
src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
print(src1.shape)
print(src2.shape)
# cv.namedWindow("example1",cv.WINDOW_AUTOSIZE)
# cv.namedWindow("example2",cv.WINDOW_AUTOSIZE)
cv.namedWindow("example",cv.WINDOW_AUTOSIZE)
# cv.imshow("example1",src1)
# cv.imshow("example2",src2)
cv.imshow("example",src)
contrast_brightness_demo(src,1.0,50)
# add_demo(src1,src2)
# subtract_demo(src1,src2)
# divide_demo(src1,src2)
# mul_demo(src1,src2)
cv.waitKey(0)
cv.destroyAllWindows()