import cv2 as cv
import numpy as np


def open_demo():
    src = cv.imread("fill.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("input", src)

    # 图像二值化
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imwrite("binary1.png", binary)
    cv.imshow("binary1", binary)

    # 开操作
    se1 = cv.getStructuringElement(cv.MORPH_RECT, (15, 1))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, se1)
    cv.imshow("binary", binary)
    cv.imwrite("binary2.png", binary)

    # 提取轮廓
    out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        x, y, w, h = cv.boundingRect(contours[c])
        y = y - 10
        h = 12
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)
    cv.imshow("result", src)


def close_demo():
    src = cv.imread("morph3.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("input", src)

    # 图像二值化
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    # 闭操作
    se = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15), (-1, -1))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, se)
    cv.imwrite("close.png", binary)
    cv.imshow("close", binary)

#open_demo()
close_demo()
cv.waitKey(0)
cv.destroyAllWindows()
