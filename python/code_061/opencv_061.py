import cv2 as cv
import numpy as np


src = cv.imread("coins.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)
dp = 1
param1 = 100
param2 = 50


circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp, 10, None, param1, param2, 20, 100)
for c in circles[0,:]:
    print(c)
    cx, cy, r = c
    cv.circle(src, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
    cv.circle(src, (cx, cy), r, (0, 0, 255), 2, 8, 0)


# show
cv.imshow("hough line demo", src)
cv.imwrite("contours_analysis.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


