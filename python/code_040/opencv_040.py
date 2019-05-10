import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

T = 127

# 转换为灰度图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
h, w = gray.shape
T = cv.mean(gray)[0]
print("current threshold value : ", T)

# 二值图像
binary = np.zeros((h, w), dtype=np.uint8)
for row in range(h):
    for col in range(w):
        pv = gray[row, col]
        if pv > T:
            binary[row, col] = 255
        else:
            binary[row, col] = 0
cv.imshow("binary", binary)

cv.waitKey(0)
cv.destroyAllWindows()


