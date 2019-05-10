import cv2 as cv
import numpy as np


src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

dst = cv.medianBlur(src, 5)
cv.imshow("blur ksize=5", dst)

cv.waitKey(0)
cv.destroyAllWindows()


