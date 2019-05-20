import cv2 as cv
import numpy as np

src = cv.imread("mask.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("binary", binary)

# 轮廓发现
image = np.zeros(src.shape, dtype=np.float32)
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
h, w = src.shape[:2]
for row in range(h):
    for col in range(w):
        dist = cv.pointPolygonTest(contours[0], (col, row), True)  # True的话返回点到轮廓的距离，False则返回+1，0，-1三个值，其中+1表示点在轮廓内部，0表示点在轮廓上，-1表示点在轮廓外
        if dist == 0:
            image[row, col] = (255, 255, 255)
        if dist > 0:
            image[row, col] = (255-dist, 0, 0)
        if dist < 0:
            image[row, col] = (0, 0, 255+dist)

dst = cv.convertScaleAbs(image)  # 将像素点进行绝对值计算
dst = np.uint8(dst)

# 显示
cv.imshow("contours_analysis", dst)
cv.imwrite("contours_analysis.png", dst)
cv.waitKey(0)
cv.destroyAllWindows()


