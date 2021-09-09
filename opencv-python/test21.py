import cv2 as cv
import numpy as np


def watershed_demo():
    # remove noise if any
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)
    # gray->binary
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary_demo", binary)
    # erode/dilate
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary_close = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=3)
    binary_dilate_dst = cv.dilate(binary_close, kernel, iterations=3)
    cv.imshow("watershed_demo", binary_dilate_dst)
    # distance
    dist = cv.distanceTransform(binary_close, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance_demo", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface_demo", surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(binary_dilate_dst, surface_fg)
    ret, markers = cv.connectedComponents(binary_dilate_dst)
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("result", src)


src = cv.imread("/Users/liuxuwei/Desktop/picture/smarties.png")
cv.namedWindow("example", cv.WINDOW_AUTOSIZE)
cv.imshow("example", src)
watershed_demo()
cv.waitKey(0)
cv.destroyAllWindows()