import cv2 as cv
import numpy as np

capture = cv.VideoCapture("test.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)


def process(image, opt=1):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    line = cv.getStructuringElement(cv.MORPH_RECT, (15, 15), (-1, -1))
    #mask = cv.inRange(hsv, (0, 43, 46), (10, 255, 255))
    cv.imshow("mask", mask)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)
    #cv.imshow("masks", mask)

    # 轮廓提取, 发现最大轮廓
    out, contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    index = -1
    max = 0
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area > max:
            max = area
            index = c
    # 绘制
    if index >= 0:
        rect = cv.minAreaRect(contours[index])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image


while(True):
    ret, frame = capture.read()
    if ret is True:
        cv.imshow("video-input", frame)
        result = process(frame)
        cv.imshow("result", result)
        c = cv.waitKey(50)
        #print(c)
        if c == 27:  #ESC
            cv.imwrite("result.jpg", result)
            break
    else:
        break
cv.waitKey(0)
cv.destroyAllWindows()

