import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')

# 角点检测参数
feature_params = dict(maxCorners=100, qualityLevel=0.01, minDistance=10, blockSize=3)

# KLT光流参数
lk_params = dict(winSize=(31, 31), maxLevel=3, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 30, 0.01))

# 随机颜色
color = np.random.randint(0,255,(100,3)) #shape(100,3)

# 读取第一帧
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# for pt in p0:
#     print(pt)
#     b = np.random.random_integers(0, 256)
#     g = np.random.random_integers(0, 256)
#     r = np.random.random_integers(0, 256)
#     x = np.int32(pt[0][0])
#     y = np.int32(pt[0][1])
#     cv.circle(old_frame, (x, y), 5, (int(b), int(g), int(r)), 2)
# cv.imshow('s',old_frame)
# cv.waitKey(0)

# 光流跟踪
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 计算光流
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # 根据状态选择
    good_new = p1[st == 1]
    good_old = p0[st == 1]

    # 绘制跟踪线
    for i, (new, old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        frame = cv.line(frame, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
    cv.imshow('frame',frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

    # 更新
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cv.destroyAllWindows()
cap.release()