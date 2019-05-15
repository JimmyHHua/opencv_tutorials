import cv2 as cv
import numpy as np

src = cv.imread("contours.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

# 轮廓发现
out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    result = cv.approxPolyDP(contours[c], 4, True)
    vertexes = result.shape[0]
    if vertexes == 3:
        cv.putText(src, "triangle", (np.int32(cx), np.int32(cy)),
                   cv.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8);
    if vertexes == 4:
        cv.putText(src, "rectangle", (np.int32(cx), np.int32(cy)),
                   cv.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8);
    if vertexes == 6:
        cv.putText(src, "poly", (np.int32(cx), np.int32(cy)),
                   cv.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8);
    if vertexes > 10:
        cv.putText(src, "circle", (np.int32(cx), np.int32(cy)),
                   cv.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8);
    print(vertexes)


# 显示
cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


