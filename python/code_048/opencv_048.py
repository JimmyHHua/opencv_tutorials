import cv2 as cv
import numpy as np


def threshold_demo(image):
    # 去噪声+二值化
    dst = cv.GaussianBlur(image,(3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow("binary", binary)
    return binary


def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output


src = cv.imread("yuan_test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
binary = threshold_demo(src)
canny = canny_demo(src)

# 轮廓发现
out, contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

# 显示
cv.imshow("contours-demo", src)

cv.waitKey(0)
cv.destroyAllWindows()


