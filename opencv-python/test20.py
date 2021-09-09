import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cv.imshow("top_hat", dst)
    # 提升亮度
    # cimage = np.array(gray.shape, np.uint8)
    # cimage = 100
    # dst = cv.add(dst, cimage)
    # cv.imshow("top_hat_add", dst)


def black_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("black_hat", dst)
    # 提升亮度
    # cimage = np.array(gray.shape, np.uint8)
    # cimage = 100
    # dst = cv.add(dst, cimage)
    # cv.imshow("top_hat_add", dst)


def top_hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary, cv.MORPH_TOPHAT, kernel)
    cv.imshow("top_ha_binaryt", dst)
    # 提升亮度
    # cimage = np.array(gray.shape, np.uint8)
    # cimage = 100
    # dst = cv.add(dst, cimage)
    # cv.imshow("top_hat_add", dst)


def black_hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("black_hat_binary", dst)
    # 提升亮度
    # cimage = np.array(gray.shape, np.uint8)
    # cimage = 100
    # dst = cv.add(dst, cimage)
    # cv.imshow("top_hat_add", dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("hat_binary", dst)


def tidu_binary_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(image, kernel)
    cv.imshow("dilate", dm)
    em = cv.erode(image, kernel)
    cv.imshow("erode", em)
    dst1 = cv.subtract(image, em) # internal
    dst2 = cv.subtract(dm, image) # external
    cv.imshow("internal_demo", dst1)
    cv.imshow("external_demo", dst2)


src = cv.imread("/Users/liuxuwei/Desktop/picture/lena.jpg")
cv.namedWindow("example", cv.WINDOW_AUTOSIZE)
cv.imshow("example", src)
# black_hat_demo(src)
# black_hat_binary_demo(src)
# top_hat_demo(src)
# top_hat_binary_demo(src)
# hat_binary_demo(src)
tidu_binary_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()