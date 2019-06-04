import numpy as np
import cv2 as cv

cap = cv.VideoCapture('color_object.mp4')
fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=1000, detectShadows=False)
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()
    cv.imshow('input', frame)
    cv.imshow('mask',fgmask)
    cv.imshow('background', background)
    k = cv.waitKey(10)&0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()