import numpy as np
import cv2 as cv

cap = cv.VideoCapture('vtest.avi')
fgbg = cv.createBackgroundSubtractorMOG2(
    history=500, varThreshold=100, detectShadows=False)


def process(image, opt=1):
    mask = fgbg.apply(frame)
    line = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)
    cv.imshow("mask", mask)
    # 轮廓提取, 发现最大轮廓
    out, contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv.minAreaRect(contours[c])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image, mask


while True:
    ret, frame = cap.read()
    cv.imwrite("input.png", frame)
    cv.imshow('input', frame)
    result, m_ = process(frame)
    cv.imshow('result', result)
    k = cv.waitKey(50)&0xff
    if k == 27:
        cv.imwrite("result.png", result)
        cv.imwrite("mask.png", m_)

        break
cap.release()
cv.destroyAllWindows()