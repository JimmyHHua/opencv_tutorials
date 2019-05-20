import cv2 as cv
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t * 2)
    cv.imwrite("canny_output.png", canny_output)
    return canny_output


src = cv.imread("twolines.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

binary = canny_demo(src)
k = np.ones((3, 3), dtype=np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, k)
cv.imshow("binary", binary)

# 轮廓发现
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 直线拟合与极值点寻找
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    m = max(w, h)
    # if m < 30:
    #     continue
    vx, vy, x0, y0 = cv.fitLine(contours[c], cv.DIST_L1, 0, 0.01, 0.01)
    k = vy/vx
    b = y0 - k*x0
    maxx = 0
    maxy = 0
    miny = 100000
    minx = 0
    for pt in contours[c]:
        px, py = pt[0]
        if maxy < py:
            maxy = py
        if miny > py:
            miny = py
    maxx = (maxy - b) / k
    minx = (miny - b) / k
    cv.line(src, (np.int32(maxx), np.int32(maxy)),
            (np.int32(minx), np.int32(miny)), (0, 0, 255), 2, 8, 0)


# 显示
cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)

cv.waitKey(0)
cv.destroyAllWindows()


