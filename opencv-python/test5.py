import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    return pv


def gaussian_noise(image):
    h, w, ch = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            for c in range(ch):
                pixel = image[row, col, c]
                image[row, col, c] = clamp(pixel + s[c])
    cv.imshow("gaussian_noise",image)


src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")

cv.imshow("src", src)

dst1 = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("G_test1", dst1)

# 经过添加高斯噪声之后 src图像已经发生了改变，即改变了内存中的原图
t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
print("%f 秒" % ((t2-t1)/cv.getTickFrequency()))

cv.imshow("src1", src)

dst2 = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("G_test2", dst2)

cv.waitKey(0)
cv.destroyAllWindows()