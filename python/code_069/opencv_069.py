import cv2 as cv

src = cv.imread("hist_01.jpg",0)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 形态学梯度 - 基本梯度
se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
basic = cv.morphologyEx(src, cv.MORPH_GRADIENT, se)
cv.imshow("basic gradient", basic)

# 外梯度
dilate = cv.morphologyEx(src, cv.MORPH_DILATE, se)
exteral = cv.subtract(dilate, src)
cv.imshow("external gradient", exteral)

# 内梯度
erode = cv.morphologyEx(src, cv.MORPH_ERODE, se)
interal = cv.subtract(src, erode)
cv.imshow("interal gradient", interal)

cv.imwrite("gradient.png", basic)
cv.imwrite("external.png", exteral)
cv.imwrite("interal.png", interal)
cv.waitKey(0)
cv.destroyAllWindows()