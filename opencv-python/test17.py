import cv2 as cv
import numpy as np


def measure_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 250, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshhold value : %s" % ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h)/max(w, h)
        print("contour rate : %s" %rate )
        mm = cv.moments(contour)
        # print(type(mm))
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 2, (0, 0, 255), -1)
        # cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contours area: %s" % area )
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] >= 10:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
    cv.imshow("measure_demo", dst)
        

src = cv.imread("/Users/liuxuwei/Desktop/picture/pic3.png")
cv.namedWindow("example", cv.WINDOW_FREERATIO)
cv.imshow("example", src)
measure_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()