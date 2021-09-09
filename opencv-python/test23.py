import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess

def recognize_test():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 3))
    binary_open = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 5))
    binary_open1 = cv.morphologyEx(binary_open, cv.MORPH_OPEN, kernel)
    cv.imshow("binary", binary_open1)
    cv.bitwise_not(binary_open1, binary_open1)
    textImage = Image.fromarray(binary_open1)
    text = tess.image_to_string(textImage)
    print("识别结果： %s" % text)


src = cv.imread("/Users/liuxuwei/Desktop/4.png")
cv.namedWindow("example", cv.WINDOW_AUTOSIZE)
cv.imshow("example", src)
recognize_test()
cv.waitKey(0)
cv.destroyAllWindows()