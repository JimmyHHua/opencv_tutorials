import cv2 as cv
import numpy as np

yolo_tiny_model = "../model/yolov3-tiny-coco/yolov3-tiny.weights";
yolo_tiny_cfg = "../model/yolov3-tiny-coco/yolov3-tiny.cfg";

# Load names of classes
classes = None
with open("../model/yolov3-tiny-coco/object_detection_classes_yolov3.txt", 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# load tensorflow model
net = cv.dnn.readNetFromDarknet(yolo_tiny_cfg, yolo_tiny_model)
# set back-end
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

cap = cv.VideoCapture()
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
vw_out = cv.VideoWriter("1.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 10, (np.int(width), np.int(height)), True)
index = 0
while True:
    ret, image = cap.read()
    if ret is False:
        break
    image = cv.flip(image, 1)
    h, w = image.shape[:2]
    # 基于多个Region层输出getUnconnectedOutLayersNames
    blobImage = cv.dnn.blobFromImage(image, 1.0/255.0, (416, 416), None, True, False);
    outNames = net.getUnconnectedOutLayersNames()
    net.setInput(blobImage)
    outs = net.forward(outNames)

    # Put efficiency information.
    t, _ = net.getPerfProfile()
    fps = 1000 / (t * 1000.0 / cv.getTickFrequency())
    label = 'FPS: %.2f' % fps
    cv.putText(image, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    # 绘制检测矩形
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            # numbers are [center_x, center_y, width, height]
            if confidence > 0.5:
                center_x = int(detection[0] * w)
                center_y = int(detection[1] * h)
                width = int(detection[2] * w)
                height = int(detection[3] * h)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # 使用非最大抑制
    indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        cv.rectangle(image, (left, top), (left+width, top+height), (0, 0, 255), 2, 8, 0)
        cv.putText(image, classes[classIds[i]], (left, top),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
    c = cv.waitKey(1)
    if c == 27:
        break
    index += 1
    if 100 < index < 200:
        vw_out.write(image)
    cv.imshow('YOLOv3-tiny-Detection-Demo', image)
cv.waitKey(0)
cv.destroyAllWindows()