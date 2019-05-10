import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# sigma = 5、15、25
blur_img = cv.GaussianBlur(src, (0, 0), 5)
usm = cv.addWeighted(src, 1.5, blur_img, -0.5, 0)
cv.imshow("mask image", usm)

h, w = src.shape[:2]
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = usm
cv.putText(result, "original image", (10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.putText(result, "sharpen image", (w+10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.imshow("sharpen_image", result)
cv.imwrite("./result.png", result)

cv.waitKey(0)
cv.destroyAllWindows()
