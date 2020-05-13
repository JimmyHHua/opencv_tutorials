import cv2
import numpy as np

bin_model = "../model/google/bvlc_googlenet.caffemodel"
protxt = "../model/google/bvlc_googlenet.prototxt"

# Load names of classes
# classes = None
# with open("classification_classes_ILSVRC2012.txt", 'rt') as f:
#     classes = f.read().rstrip('\n').split('\n')

# print(classes)

# load CNN model
net = cv2.dnn.readNet(bin_model, protxt)

# 获取各层信息
layer_names = net.getLayerNames()

for name in layer_names:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id : %d, type : %s, name: %s"%(id, layer.type, layer.name))

print("successfully loaded model...")