import cv2 as cv
import numpy as np


src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

dst1 = cv.blur(src, (5, 5))
dst2 = cv.GaussianBlur(src, (5, 5), sigmaX=15)
dst3 = cv.GaussianBlur(src, (0, 0), sigmaX=15)

cv.imshow("blur ksize=5", dst1)
cv.imshow("gaussian ksize=5", dst2)
cv.imshow("gaussian sigmax=15", dst3)

cv.waitKey(0)
cv.destroyAllWindows()


