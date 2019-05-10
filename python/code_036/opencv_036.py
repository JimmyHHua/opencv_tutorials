import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# t1 = 100, t2 = 3*t1 = 300
edge = cv.Canny(src, 100, 300)
cv.imshow("mask image", edge)
cv.imwrite("./edge.png", edge)
edge_src = cv.bitwise_and(src, src, mask=edge)

h, w = src.shape[:2]
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = edge_src
cv.putText(result, "original image", (10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.putText(result, "edge image", (w+10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.imshow("edge detector", result)
cv.imwrite("./result.png", result)

cv.waitKey(0)
cv.destroyAllWindows()
