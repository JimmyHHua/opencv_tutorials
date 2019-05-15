import cv2 as cv
import numpy as np


def contours_info(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours


src = cv.imread("abc.png")
cv.namedWindow("input1", cv.WINDOW_AUTOSIZE)
cv.imshow("input1", src)
src2 = cv.imread("a5.png")
cv.imshow("input2", src2)

# 轮廓发现
contours1 = contours_info(src)
contours2 = contours_info(src2)

# 几何矩计算与hu矩计算
mm2 = cv.moments(contours2[0])
hum2 = cv.HuMoments(mm2)

# 轮廓匹配
for c in range(len(contours1)):
    mm = cv.moments(contours1[c])
    hum = cv.HuMoments(mm)
    dist = cv.matchShapes(hum, hum2, cv.CONTOURS_MATCH_I1, 0)
    if dist < 1:
        cv.drawContours(src, contours1, c, (0, 0, 255), 2, 8)
    print("dist %f"%(dist))

# 显示
cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


