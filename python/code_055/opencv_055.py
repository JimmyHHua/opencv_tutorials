import cv2 as cv
import numpy as np

src = cv.imread("hand.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
k = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

# 开运算去除外部噪点
binary = cv.morphologyEx(binary, cv.MORPH_OPEN, k)
cv.imshow("binary", binary)

# 轮廓发现
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
for c in range(len(contours)):
    ret = cv.isContourConvex(contours[c])
    points = cv.convexHull(contours[c])
    #cv.polylines(src, [points], True, (0, 255, 0), 2)
    total = len(points)
    print(total)
    for i in range(len(points)):
        x1, y1 = points[i][0]
        x2, y2 = points[(i+1)%total][0]
        cv.circle(src, (x1, y1), 4, (255, 0, 0), 2, 8, 0)
        cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
    print(points)
    print("convex : ", ret)


# 显示
cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


