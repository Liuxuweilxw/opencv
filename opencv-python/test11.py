import cv2 as cv
import numpy as np

# 图像金字塔
def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_demo_" + str(i),dst)
        temp = dst.copy()
    return pyramid_images


def lpls_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if i==0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lpls" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], expand)
            cv.imshow("lpls" + str(i), lpls)




src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
# cv.namedWindow("example",cv.WINDOW_AUTOSIZE)
# cv.imshow("example",src)
# ！！！仅适用于2的n次幂尺寸的图片
lpls_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()