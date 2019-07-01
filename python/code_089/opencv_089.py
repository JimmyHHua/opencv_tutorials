import cv2 as cv
import numpy as np

cap = cv.VideoCapture('test.mp4')

# 读取第一帧
ret,frame = cap.read()
cv.namedWindow("Demo", cv.WINDOW_AUTOSIZE)

# 选择ROI区域
x, y, w, h = cv.selectROI("Demo", frame, True, False)
track_window = (x, y, w, h)

# 获取ROI直方图
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, (26, 43, 46), (34, 255, 255))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

# 设置迭代的终止标准，最多十次迭代
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
while True:
    ret, frame = cap.read()
    if ret is False:
        break;
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)

    # 搜索更新roi区域
    ret, track_box = cv.CamShift(dst, track_window, term_crit)

    # 可变角度的矩形框
    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    cv.polylines(frame, [pts], True, (0, 255, 0), 2)

    # 更新窗口
    track_window = track_box
    #print(track_box)
    # 绘制窗口CAM，目标椭圆图
    cv.ellipse(frame, ret, (0, 0, 255), 3, 8)
    cv.imshow('Demo',frame)
    k = cv.waitKey(50) & 0xff
    if k == 27:
        break
    else:
        cv.imwrite(chr(k)+".jpg",frame)

cv.destroyAllWindows()
cap.release()