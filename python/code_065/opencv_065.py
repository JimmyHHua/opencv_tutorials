import cv2 as cv
import numpy as np

src = cv.imread("cells.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 高斯模糊去噪声
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imwrite("binary1.png", binary)
cv.imshow("binary1", binary)

# 闭操作
se1 = cv.getStructuringElement(cv.MORPH_RECT, (25, 5), (-1, -1))
se2 = cv.getStructuringElement(cv.MORPH_RECT, (5, 25), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, se1)
binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, se2)

cv.imshow("binary", binary)
cv.imwrite("binary2.png", binary)

cv.waitKey(0)
cv.destroyAllWindows()
