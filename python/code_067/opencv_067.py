import cv2 as cv
import numpy as np

src = cv.imread("morph02.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 高斯模糊去噪声
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

# 顶帽操作
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_TOPHAT, se)


cv.imshow("binary", binary)
cv.imwrite("binary3.png", binary)

cv.waitKey(0)
cv.destroyAllWindows()
