import cv2 as cv
import numpy as np

src = cv.imread("coins.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)

# 二值化图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("input", binary)

# 使用3x3结构元素进行膨胀与腐蚀操作
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
dilate = cv.dilate(binary, se, None, (-1, -1), 1)
erode = cv.erode(binary, se, None, (-1, -1), 1)

# 显示
cv.imshow("dilate", dilate)
cv.imshow("erode", erode)
cv.imwrite("dilate.png", dilate)
cv.imwrite("erode.png", erode)
cv.waitKey(0)
cv.destroyAllWindows()
