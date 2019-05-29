import cv2 as cv
import numpy as np

src = cv.imread("case6.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 图像二值化
# src = cv.GaussianBlur(src, (5, 5), 0)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, se)
cv.imshow("binary", binary)

# 轮廓提取
out, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
index = 0
max = 0
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    if h >=height or w >= width:
        continue
    area = cv.contourArea(contours[c])
    if area > max:
        max = area
        index = c

print(index)

# 绘制轮廓关键点与轮廓
result = np.zeros(src.shape, dtype=np.uint8)
keypts = cv.approxPolyDP(contours[index], 4, True)
cv.drawContours(src, contours, index, (0, 0, 255), 1, 8)
cv.drawContours(result, contours, index, (0, 0, 255), 1, 8)
#print(keypts)
for pt in keypts:
    cv.circle(src, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2, 8, 0)
    cv.circle(result, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2, 8, 0)
cv.imshow("result", result)
cv.imshow("output", src)
cv.imwrite("result.png", result)
cv.imwrite("output.png", src)

cv.waitKey(0)
cv.destroyAllWindows()