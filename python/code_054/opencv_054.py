import cv2 as cv
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    cv.imwrite("canny_output.png", canny_output)
    return canny_output


src = cv.imread("stuff.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
binary = canny_demo(src)
k = np.ones((3, 3), dtype=np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, k)

# 轮廓发现
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    # 椭圆拟合
    (cx, cy), (a, b), angle = cv.fitEllipse(contours[c])
    # 绘制椭圆
    cv.ellipse(src, (np.int32(cx), np.int32(cy)),
               (np.int32(a/2), np.int32(b/2)), angle, 0, 360, (0, 0, 255), 2, 8, 0)


# 显示
cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


