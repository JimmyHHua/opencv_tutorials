import cv2 as cv
cap = cv.VideoCapture('test.mp4')

# 读取第一帧
ret,frame = cap.read()
cv.namedWindow("CAS Demo", cv.WINDOW_AUTOSIZE)
# 可以在图片上选择roi区域
x, y, w, h = cv.selectROI("CAS Demo", frame, True, False)
track_window = (x, y, w, h)

# 获取ROI直方图
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, (26, 43, 46), (34, 255, 255))

# 计算直方图,参数为 图片(可多)，通道数，蒙板区域，直方图长度，范围
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

    # 均值迁移，搜索更新roi区域
    ret, track_window = cv.meanShift(dst, track_window, term_crit)
    # 绘制窗口
    x,y,w,h = track_window
    cv.rectangle(frame, (x,y), (x+w,y+h), 255,2)
    cv.imshow('CAS Demo',frame)
    k = cv.waitKey(60) & 0xff
    if k == 27:
        break
    else:
        cv.imwrite(chr(k)+".jpg",frame)
cv.destroyAllWindows()
cap.release()

