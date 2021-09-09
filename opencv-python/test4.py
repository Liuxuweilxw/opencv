import cv2 as cv
import numpy as np


# 均值模糊
def blur_demo(image):
    dst=cv.blur(image,(3,3))
    cv.imshow("blur_demo",dst)


# 中值模糊，对椒盐噪声有很好的去除效果
def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("median_blur_demo",image)

# 自定义模糊
# kernel核 必须为奇数
def custom_blur_demo(image):
    # 模糊
    # kernel = np.ones([5,5],np.float32)/25
    # 锐化
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)
    # cv.filter2D(src,ddepth,kernel,dst,anchor,delta,borderType)
    #             源图片，图片深度（-1为默认值，即与原图一致），kernel(卷积核size),dst(目标输出)，anchor（锚点）
    dst = cv.filter2D(image,-1,kernel)
    cv.imshow("custom_blur_demo",dst)


src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
cv.namedWindow("example")
cv.imshow("example",src)
#均值模糊
blur_demo(src)
#中值模糊
median_blur_demo(src)
#自定义模糊
custom_blur_demo(src)


cv.waitKey(0)
cv.destroyAllWindows()