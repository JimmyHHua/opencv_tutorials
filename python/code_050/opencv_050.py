import cv2 as cv
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    cv.imwrite("canny_output.png", canny_output)
    return canny_output


src = cv.imread("zhifang_ball.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
binary = canny_demo(src)
k = np.ones((3, 3), dtype=np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, k)

# 轮廓发现
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    # x, y, w, h = cv.boundingRect(contours[c]);
    # cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)
    # cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0);
    area = cv.contourArea(contours[c]) # 计算面积
    arclen = cv.arcLength(contours[c], True) #计算弧长， True表示闭合区域
    if area < 100 or arclen < 100:
        continue
    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(src,[box],0,(0,0,255),2)
    cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)


# 显示
cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


