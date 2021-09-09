import cv2 as cv
import numpy as np


def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary_demo", binary)
    contours, b = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print()
    cv.imshow("detect_contours", image)


def edge_contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("edge_output_demo", edge_output)
    contours, b = cv.findContours(edge_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print()
    cv.imshow("edge_detect_contours", image)


src = cv.imread("/Users/liuxuwei/Desktop/picture/sudoku.png")
cv.namedWindow("example", cv.WINDOW_FREERATIO)
cv.imshow("example",src)
contours_demo(src)
src = cv.imread("/Users/liuxuwei/Desktop/picture/sudoku.png")
edge_contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()