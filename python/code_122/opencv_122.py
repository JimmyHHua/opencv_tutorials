import cv2
import numpy as np

bin_model = "../model/google/bvlc_googlenet.caffemodel"
protxt = "../model/google/bvlc_googlenet.prototxt"

# Load names of classes
classes = None
with open("../model/google/classification_classes_ILSVRC2012.txt", 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# load CNN model
net = cv2.dnn.readNetFromCaffe(protxt, bin_model)

# read input data
image = cv2.imread("guinea_pig.jpg")
blob = cv2.dnn.blobFromImage(image, 1.0, (224, 224), (104, 117,123), False, crop=False)
result = np.copy(image)
cv2.imshow("input", image)

# Run a model
net.setInput(blob)
out = net.forward()

# Get a class with a highest score.
out = out.flatten()
classId = np.argmax(out)
confidence = out[classId]

# Put efficiency information.
t, _ = net.getPerfProfile()
label = 'cost time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
cv2.putText(result, label, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

# Print predicted class.
label = '%s: %.4f' % (classes[classId] if classes else 'Class #%d' % classId, confidence)
cv2.putText(result, label, (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

show_img = np.hstack((image, result))
cv2.namedWindow('demo', cv2.WINDOW_NORMAL)
cv2.imshow("demo", show_img)
cv2.waitKey(0)
cv2.destroyAllWindows()