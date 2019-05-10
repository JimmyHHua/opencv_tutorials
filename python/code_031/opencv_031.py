import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

h, w = src.shape[:2]
x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)
# cv.imshow("x_grad", x_grad)
# cv.imshow("y_grad", y_grad)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("gradient", dst)

result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = dst
cv.imshow("result", result)
cv.imwrite("./result.png", dst)

cv.waitKey(0)
cv.destroyAllWindows()
