import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 直方图
def plot_demo(image):
    plt.hist(image.ravel(), 256, [0,256])
    plt.show()


def image_hist(image):
    color = ("blue","green","red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0,256])
        plt.plot(hist,color)
        plt.xlim([0,256])
    plt.show()


src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
cv.namedWindow("example",cv.WINDOW_AUTOSIZE)

cv.imshow("example",src)
# plot_demo(src)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()
