import cv2 as cv
import numpy as np

src = cv.imread("LinuxLogo.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 使用3x3结构元素进行膨胀与腐蚀操作
se = np.ones((3, 3), dtype=np.uint8)
dilate = cv.dilate(src, se, None, (-1, -1), 1)
erode = cv.erode(src, se, None, (-1, -1), 1)

# 显示
cv.imshow("dilate", dilate)
cv.imshow("erode", erode)
cv.imwrite("dilate.png", dilate)
cv.imwrite("erode.png", erode)
cv.waitKey(0)
cv.destroyAllWindows()
