import cv2

inference_pb = "../faster_rcnn_resnet50_coco_2018_01_28/frozen_inference_graph.pb";
graph_text = "../faster_rcnn_resnet50_coco_2018_01_28/graph.pbtxt";

# load tensorflow model
net = cv2.dnn.readNetFromTensorflow(inference_pb, graph_text)
image = cv2.imread("cat.jpg")
h = image.shape[0]
w = image.shape[1]

# 检测
net.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False))
cvOut = net.forward()
for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.5:
        left = detection[3]*w
        top = detection[4]*h
        right = detection[5]*w
        bottom = detection[6]*h

        # 绘制
        cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), thickness=2)
        cv2.putText(image, "score:%.2f"%score, (int(left), int(top)-2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
cv2.imshow('faster-rcnn-demo', image)
cv2.imwrite('result_cat.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()