import cv2 as cv
import numpy as np

base_dir = "../model/fast_style/"
styles = ["composition_vii.t7", "starry_night.t7", "la_muse.t7", "the_wave.t7",
          "mosaic.t7", "the_scream.t7", "feathers.t7", "candy.t7", "udnie.t7"]
index = 6
net = cv.dnn.readNetFromTorch(base_dir + styles[index])
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV);
cap = cv.VideoCapture(0)
while cv.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv.waitKey()
        break
    cv.imshow("frame", frame)
    inWidth = 256
    inHeight = 256
    h, w = frame.shape[:2]
    inp = cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                              (103.939, 116.779, 123.68), swapRB=False, crop=False)

    # 执行风格迁移
    net.setInput(inp)
    out = net.forward()
    print(out.shape)
    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    label = "FPS : %.2f" % (1000 / (t / freq))

    # 解析输出
    out = out.reshape(3, out.shape[2], out.shape[3])
    print("ddddddddd", out.shape)
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.68
    out /= 255.0
    out = out.transpose(1, 2, 0)
    print("new shape", out.shape)
    #out = np.random.random((256,256,3))
    out = np.clip(out, 0, 1)
    out = (255 * out).astype('uint8')
    # rescale与中值模糊，消除极值点噪声
    #cv.normalize(out, out, 0, 255, cv.NORM_MINMAX)

    out = cv.medianBlur(out, 5)

    # resize and show
    result = np.uint8(cv.resize(out, (w, h)))
    cv.putText(result, label, (5, 25), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv.imshow('Fast Style Demo', result)
    cv.imwrite("result_%d.png"%index, result)


