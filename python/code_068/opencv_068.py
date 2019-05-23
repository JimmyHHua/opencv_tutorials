import cv2 as cv
import numpy as np

src = cv.imread("morph.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 图像二值化
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

# 黑帽操作
se = cv.getStructuringElement(cv.MORPH_RECT, (9, 9), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, se)


cv.imshow("black hat", binary)
cv.imwrite("binary2.png", binary)

cv.waitKey(0)
cv.destroyAllWindows()