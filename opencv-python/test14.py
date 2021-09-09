import cv2 as cv
import numpy as np

# 直线检测
def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),1)
    cv.imshow("line_detection", image)


def line_detect_possible_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detect_possible_demo", image)


src = cv.imread("C:/Users/liuxuwei/Desktop/sudoku.png")
cv.namedWindow("example",cv.WINDOW_FREERATIO)
cv.imshow("example",src)
# line_detection(src)
line_detect_possible_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()


