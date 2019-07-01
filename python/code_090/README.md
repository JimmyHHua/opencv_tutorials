# 对象移动轨迹绘制

✔️ 移动对象分析，我们可以绘制对象运行轨迹曲线，这个主要是根据移动对象窗口轮廓，获取中心位置，然后使用中心位置进行绘制即可得到。

✔️ 大致的程序步骤如下：
1.  初始化路径点数组
2.  对每帧的预测轮廓提取中心位置添加到路径数组
3.  绘制路径曲线

## 代码

✔️ 我们只需要在上一节Camshift的代码中添加一个数组存储中心位置，然后使用`cv2.line()`画出即可。

修改部分：
```python
tracking_path = []
while True:
    ret, frame = cap.read()
    if ret is False:
        break;
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)

    # ，搜索更新roi区域， 保持运行轨迹
    ret, track_box = cv.CamShift(dst, track_window, term_crit)
    track_window = track_box

    # 椭圆中心
    pt = np.int32(ret[0])
    if pt[0] > 0 and pt[1] > 0:
        tracking_path.append(pt)

    # 绘制跟踪对象位置窗口与对象运行轨迹
    #cv.ellipse(frame, ret, (0, 0, 255), 3, 8)
    for i in range(1, len(tracking_path)):
        cv.line(frame, (tracking_path[i - 1][0], tracking_path[i - 1][1]),
                (tracking_path[i][0], tracking_path[i][1]), (0, 255, 0), 2, 6, 0)

    cv.imshow('Demo',frame)
    k = cv.waitKey(50) & 0xff
    if k == 27:
        break
    else:
        cv.imwrite(chr(k)+".jpg",frame)
```
<img src="https://i.loli.net/2019/07/01/5d19cceeaa88d33367.gif" alt="ss.gif" title="ss.gif" width=400/>