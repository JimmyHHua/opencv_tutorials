import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

h, w = src.shape[:2]
dst = cv.bilateralFilter(src, 0, 100, 10)
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = dst
result = cv.resize(result, (w, h//2))
cv.imshow("result", result)

cv.waitKey(0)
cv.destroyAllWindows()
