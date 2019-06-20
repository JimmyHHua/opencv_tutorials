 
#代码待补充：
import numpy as np
import cv2 as cv
import math
cap = cv.VideoCapture('car_flow.mp4')
 
#角点检测参数
feature_params = dict(maxCorners=100, qualityLevel=0.1, minDistance=7, blockSize=7)
 
#KLT光流参数
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.02))

height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv.CAP_PROP_FPS)
#out = cv.VideoWriter("reslut.avi", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps,
                     #(np.int(width), np.int(height)), True)

tracks = []
track_len = 15
frame_idx = 0
detect_interval = 5
while True:

    ret, frame = cap.read()
    if ret:
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        vis = frame.copy()

        if len(tracks)>0:
            img0 ,img1 = prev_gray, frame_gray
            p0 = np.float32([tr[-1] for tr in tracks]).reshape(-1,1,2)
            # 上一帧的角点和当前帧的图像作为输入来得到角点在当前帧的位置  
            p1, st, err = cv.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)

            # 反向检查,当前帧跟踪到的角点及图像和前一帧的图像作为输入来找到前一帧的角点位置  
            p0r, _, _ = cv.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)

            # 得到角点回溯与前一帧实际角点的位置变化关系 
            d = abs(p0-p0r).reshape(-1,2).max(-1)

            #判断d内的值是否小于1，大于1跟踪被认为是错误的跟踪点
            good = d < 1

            new_tracks = []

            for i, (tr, (x, y), flag) in enumerate(zip(tracks, p1.reshape(-1, 2), good)):

                # 判断是否为正确的跟踪点
                if not flag:
                    continue

                # 存储动态的角点
                tr.append((x, y))

                # 只保留track_len长度的数据，消除掉前面的超出的轨迹
                if len(tr) > track_len:
                    del tr[0]
                # 保存在新的list中
                new_tracks.append(tr)

                cv.circle(vis, (x, y), 2, (0, 255, 0), -1)

            # 更新特征点    
            tracks = new_tracks

            # #以上一振角点为初始点，当前帧跟踪到的点为终点,画出运动轨迹
            cv.polylines(vis, [np.int32(tr) for tr in tracks], False, (0, 255, 0), 1)


        # 每隔 detect_interval 时间检测一次特征点
        if frame_idx % detect_interval==0:
            mask = np.zeros_like(frame_gray)
            mask[:] = 255

            if frame_idx !=0:
                for x,y in [np.int32(tr[-1]) for tr in tracks]:
                    cv.circle(mask, (x, y), 5, 0, -1)
                    
            p = cv.goodFeaturesToTrack(frame_gray, mask=mask, **feature_params)
            if p is not None:
                for x, y in np.float32(p).reshape(-1,2):
                    tracks.append([(x, y)])

        frame_idx += 1
        prev_gray = frame_gray

        cv.imshow('track', vis)
        #out.write(vis)
        ch = cv.waitKey(1) & 0xff
        if ch ==27:
            cv.imwrite('track.jpg', vis)
            break
    else:
        break

cv.destroyAllWindows()
cap.release()

