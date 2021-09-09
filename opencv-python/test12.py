import cv2 as cv
import numpy as np

# 求导
def lapalian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", lpls)


def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("grad_x", gradx)
    cv.imshow("grad_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradxy", gradxy)


src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
# sobel_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()