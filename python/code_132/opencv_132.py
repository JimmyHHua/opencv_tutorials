import cv2 as cv
import numpy as np

bin_model = "../model/google/bvlc_googlenet.caffemodel"
protxt = "../model/google/bvlc_googlenet.prototxt"

# Load names of classes
classes = None
with open("../model/google/classification_classes_ILSVRC2012.txt", 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# load CNN model
net = cv.dnn.readNetFromCaffe(protxt, bin_model)

# read input data
image1 = cv.imread("cats.jpg")
image2 = cv.imread("car.jpg")
images = []
images.append(image1)
images.append(image2)
blobs = cv.dnn.blobFromImages(np.asarray(images), 1.0, (224, 224), (104, 117,123), False, crop=False)
print(blobs.shape)

# Run a model
net.setInput(blobs)
out = net.forward()
# Put efficiency information.
t, _ = net.getPerfProfile()
label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
print(out.shape)

# Get a class with a highest score.
for i in range(len(out)):
    classId = np.argmax(out[i])
    confidence = out[i][classId]
    cv.putText(images[i], label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

    # Print predicted class.
    text_label = '%s: %.4f' % (classes[classId] if classes else 'Class #%d' % classId, confidence)
    cv.putText(images[i], text_label, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv.imshow("googlenet-demo", images[i])
    cv.imwrite("%d.jpg"%i, images[i])
    cv.waitKey(0)
cv.destroyAllWindows()