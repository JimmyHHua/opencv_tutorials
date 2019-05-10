import cv2 as cv
import numpy as np

image = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", image)

h, w = image.shape[:2]
src = cv.GaussianBlur(image, (0, 0), 1)
dst = cv.Laplacian(src, cv.CV_32F, ksize=3, delta=127)
dst = cv.convertScaleAbs(dst)
result = np.zeros([h, w*2, 3], dtype=image.dtype)
result[0:h,0:w,:] = image
result[0:h,w:2*w,:] = dst
cv.imshow("result", result)
cv.imwrite("./aplacian.png", result)


cv.waitKey(0)
cv.destroyAllWindows()
