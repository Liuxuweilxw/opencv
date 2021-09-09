import cv2 as cv
import numpy as np

# 模板匹配
def template_demo():
    tpl = cv.imread("C:/Users/liuxuwei/Desktop/lena1.jpg")
    target = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
    cv.imshow("template image",tpl)
    cv.imshow("target image",target)
    # TM_SQDIFF 插值平方和匹配 越接近于0 越匹配 利用图像与模板各个像素差值的平方和来进行匹配
    # TM_CCORR 相关匹配  采用模板和图像的互相关计算作为相似度的度量方法 数值越大 越匹配
    # TM_CCOEFF 相关匹配 把图像和模板都减去了各自的平均值，使得这两幅图像都没有直流分量
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow("match" + np.str(md),target)

# def template_demo():
#     tpl = cv.imread("C:/Users/liuxuwei/Desktop/lena1.jpg")
#     target = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
#     cv.imshow("template", tpl)
#     cv.imshow("target", target)
#
#     methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  # 三种模板匹配方法
#     th, tw = tpl.shape[:2]
#
#     for md in methods:
#         print(md)
#         result = cv.matchTemplate(target, tpl, md)  # 得到匹配结果
#         min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
#         if md == cv.TM_SQDIFF_NORMED:  # cv.TM_SQDIFF_NORMED最小时最相似，其他最大时最相似
#             tl = min_loc
#         else:
#             tl = max_loc
#
#         br = (tl[0] + tw, tl[1] + th)
#         cv.rectangle(target, tl, br, (0, 0, 255), 2)  # tl为左上角坐标，br为右下角坐标，从而画出矩形
#         cv.imshow("match-"+np.str(md), target)



src = cv.imread("C:/Users/liuxuwei/Desktop/lena.jpg")
# cv.namedWindow("example")
# cv.imshow("example",src)
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()