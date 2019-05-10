import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
h, w = src.shape[:2]

# 获取ROI
cy = h//2
cx = w//2
roi = src[cy-100:cy+100,cx-100:cx+100,:]
cv.imshow("roi", roi)

# copy ROI
image = np.copy(roi)

# modify ROI
roi[:, :, 0] = 0
cv.imshow("result", src)

# modify copy roi
image[:, :, 2] = 0
cv.imshow("result", src)
cv.imshow("copy roi", image)

# example with ROI - generate mask
src2 = cv.imread("./test.png")
cv.imshow("src2", src2)
hsv = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, (35, 43, 46), (99, 255, 255))

# extract person ROI
mask = cv.bitwise_not(mask)
person = cv.bitwise_and(src2, src2, mask=mask)

# generate background
result = np.zeros(src2.shape, src2.dtype)
result[:,:,0] = 255

# combine background + person
mask = cv.bitwise_not(mask)
dst = cv.bitwise_or(person, result, mask=mask)
dst = cv.add(dst, person)

cv.imshow("dst", dst)

cv.waitKey(0)
cv.destroyAllWindows()


