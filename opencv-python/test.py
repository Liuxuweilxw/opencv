import cv2 as cv
import numpy as np


# 调用相机 或者读取视频
# Macos 下 需要通过终端打开IDE才可以调用摄像头
def get_video_info():
    capture = cv.VideoCapture(0)
    # 0 1 2... 代表摄像头 也可以填写视频文件路径
    while True:
        ret,frame = capture.read()
        # 返回两个值  ret frame
        frame = cv.flip(frame, 1)
        # cv.flip() 可以将视频图像反转
        frame_ga = cv.GaussianBlur(frame, (3, 3), 0)
        # kernel 数值越大 去噪效果越好
        # 边缘检测先经过高斯模糊去除部分噪声
        # 再经过灰度化
        # 最后边缘检测
        gray = cv.cvtColor(frame_ga, cv.COLOR_BGR2GRAY)
        dst = cv.Canny(gray, 10, 150)
        # 可以通过bitwise_and 生成彩色边框
        dst_final = cv.bitwise_and(frame, frame, mask=dst)
        cv.imshow("video", dst_final)
        c = cv.waitKey(30)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s, height: %s, channels: %s" % (width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c]=255-pv
    cv.imshow("pixel_demo",image)


# 下方法与上方法功能完全一致


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("output",dst)


def crete_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow("new image",img)


src = cv.imread("C:/Users/liuxuwei/Desktop/2.jpg")
get_video_info()
# cv.namedWindow("input image")
# cv.imshow("input image",src)
# t1 = cv.getTickCount()
# access_pixels(src)
# crete_image()
# inverse(src)
# t2 = cv.getTickCount()
# print("time: %f 秒" % ((t2-t1)/cv.getTickFrequency()))
cv.waitKey(0)
cv.destroyAllWindows()
