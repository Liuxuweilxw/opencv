import cv2 as cv
import numpy as np

# 边缘检测
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    gradx = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grady = cv.Sobel(gray,cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(gradx, grady, 50, 100)
    cv.imshow("edge_demo", edge_output)

    # dst = cv.bitwise_and(image, image, mask=edge_output)
    # cv.imshow("Color edge", dst)

# src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
# cv.namedWindow("example",cv.WINDOW_FREERATIO)
# cv.imshow("example", src)
# edge_demo(src)
# cv.waitKey(0)
# cv.destroyAllWindows()