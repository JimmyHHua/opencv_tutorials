import cv2 as cv

src = cv.imread("master2.jpg")
cv.imshow("watermark image", src)
# 提取划痕
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, (100, 43, 46), (124, 255, 255))
cv.imshow("mask", mask)
cv.imwrite("mask.png", mask)

# 消除
se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
mask = cv.dilate(mask, se)
result = cv.inpaint(src, mask, 3, cv.INPAINT_TELEA)
cv.imshow("result", result)
cv.imwrite("result.png", result)
cv.waitKey(0)
cv.destroyAllWindows()
