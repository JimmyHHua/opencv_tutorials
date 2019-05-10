import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# X Flip 倒影
dst1 = cv.flip(src, 0);
cv.imshow("x-flip", dst1);

# Y Flip 镜像
dst2 = cv.flip(src, 1);
cv.imshow("y-flip", dst2);

# XY Flip 对角
dst3 = cv.flip(src, -1);
cv.imshow("xy-flip", dst3);

# custom y-flip
h, w, ch = src.shape
dst = np.zeros(src.shape, src.dtype)
for row in range(h):
    for col in range(w):
        b, g, r = src[row, col]
        dst[row, w - col - 1] = [b, g, r]
cv.imshow("custom-y-flip", dst)

cv.waitKey(0)
cv.destroyAllWindows()


