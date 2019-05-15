import cv2 as cv
import numpy as np


def method_1(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    t, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    return binary


def method_2(image):  
    blurred = cv.GaussianBlur(image, (3, 3), 0) # 高斯去噪音
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    t, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    return binary


def method_3(image): 
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)  # 先均值迁移去噪声
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    t, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    return binary


src = cv.imread("coins.jpg")
h, w = src.shape[:2]
ret = method_3(src)

result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2*w,:] = cv.cvtColor(ret, cv.COLOR_GRAY2BGR)
cv.putText(result, "input", (10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.putText(result, "binary", (w+10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.imshow("result", result)
cv.imwrite("binary_result.png", result)

cv.waitKey(0)
cv.destroyAllWindows()


