import cv2 as cv
import numpy as np
#
# THRESH_BINARY = 0
# THRESH_BINARY_INV = 1
# THRESH_TRUNC = 2
# THRESH_TOZERO = 3
# THRESH_TOZERO_INV = 4
#
src = cv.imread("master.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

T = 127

# 转换为灰度图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)

cv.waitKey(0)
cv.destroyAllWindows()


