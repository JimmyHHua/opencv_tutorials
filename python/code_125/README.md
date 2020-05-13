## SSD实现目标检测

✔️ OpenCV的DNN模块支持常见得对象检测模型SSD， 以及Mobile Net-SSD。

✔️ 这里我们用基于Caffe训练好的mobile-net SSD来测试目标检测。


### 视频检测

修改代码部分如下
```python
# 调用前置摄像头获取视频
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    h, w = frame.shape[:2]
    blobImage = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False);
    net.setInput(blobImage)
    cvOut = net.forward()
    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        objIndex = int(detection[1])
        if score > 0.5:
            left = detection[3]*w
            top = detection[4]*h
            right = detection[5]*w
            bottom = detection[6]*h

            # 绘制
            cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness=2)
            cv2.putText(frame, "score:%.2f, %s"%(score, objName[objIndex]),
                    (int(left) - 10, int(top) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8);
    cv2.imshow('video-ssd-demo', frame)
    c = cv2.waitKey(10)
    if c == 27:
        break
```