import numpy as np
import cv2 as cv

cap = cv.VideoCapture("bike.avi")
ret, prevFrame = cap.read()
prevGray = cv.cvtColor(prevFrame, cv.COLOR_BGR2GRAY)
prevGray = cv.GaussianBlur(prevGray, (0, 0), 15)
k = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (0, 0), 15)
    # 两帧法
    diff = cv.subtract(gray, prevGray)
    t, binary = cv.threshold(diff, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, k)
    cv.imshow('input', frame)
    cv.imshow('result', binary)
    cv.imwrite("result.png", binary)
    c = cv.waitKey(50)&0xff
    prevGray = np.copy(gray)
    if c == 27:
        break
cap.release()
cv.destroyAllWindows()