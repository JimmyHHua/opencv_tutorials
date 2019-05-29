import cv2 as cv
import numpy as np

src = cv.imread("cross.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# Binary image
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

# Hit and Miss
se = cv.getStructuringElement(cv.MORPH_CROSS, (12, 12))
binary = cv.morphologyEx(binary, cv.MORPH_HITMISS, se)


cv.imshow("hit miss", binary)
cv.imwrite("binary2.png", binary)

cv.waitKey(0)
cv.destroyAllWindows()