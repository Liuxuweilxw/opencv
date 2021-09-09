import cv2 as cv
import numpy as np


# 整体阈值 二值化
def threshold_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 100, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value %s" % ret)
    cv.imshow("binary", binary)


# 局部阈值 自适应二值化
def local_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary",dst)


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row:row+ch, col:col+cw] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("C:/Users/liuxuwei/Desktop/a.png",gray)


src = cv.imread("C:/Users/liuxuwei/Desktop/big.JPG")
# cv.namedWindow("example")
# cv.imshow("example",src)
# threshold_demo(src)
# local_threshold(src)
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()