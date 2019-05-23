import cv2 as cv

src = cv.imread("kd02.png")
src = cv.resize(src,(800,300),interpolation=cv.INTER_CUBIC)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 形态学梯度 - 基本梯度
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
basic = cv.morphologyEx(src, cv.MORPH_GRADIENT, se)
cv.imshow("basic gradient", basic)

gray = cv.cvtColor(basic, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("binary", binary)

se = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, se)
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    area = cv.contourArea(contours[c])
    if area < 200:
        continue
    if h > (3*w) or h < 20:
        continue
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)

cv.imshow("result", src)
cv.waitKey(0)
cv.destroyAllWindows()