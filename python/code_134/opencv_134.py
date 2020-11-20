import cv2 as cv
import numpy as np

# load CNN model
bin_model = "../model/enet/model-best.net";
net = cv.dnn.readNetFromTorch(bin_model)
# read input data
frame = cv.imread("street.jpg")
frame = cv.resize(frame,(0,0), fx=0.5, fy=0.5)
blob = cv.dnn.blobFromImage(frame, 0.00392, (512, 256), (0, 0, 0), True, False);
cv.imshow("input", frame)
h, w, c = frame.shape

# Run a model
net.setInput(blob)
score = net.forward()
# Put efficiency information.
t, _ = net.getPerfProfile()
label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
score = np.squeeze(score)
score = score.transpose((1, 2, 0))
score = np.argmax(score, 2)
mask = np.uint8(score)
mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
cv.normalize(mask, mask, 0, 255, cv.NORM_MINMAX)
cmask = cv.applyColorMap(mask, cv.COLORMAP_JET)
cmask = cv.resize(cmask, (w, h))
dst = cv.addWeighted(frame, 0.7, cmask, 0.3, 0)
cv.putText(dst, label, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
cv.imshow("dst", dst)
cv.imwrite("enet_result.png", dst)
cv.waitKey(0)
cv.destroyAllWindows()