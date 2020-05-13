## 读取DNN模型各层信息

### 概述
 ✔️ OpenCV的DNN模块支持下面框架的预训练模型的前馈网络(预测图)使用：
- Caffe
- Tensorflow
- Torch
- DLDT
- Darknet

同时还支持自定义层解析、非最大抑制操作、获取各层的信息等。
OpenCV加载模型的通用API为:
```
cv2.dnn.readNet(model,  # 模型
            	config = "", 
            	framework = "" )
```
其中：
- model二进制训练好的网络权重文件，可能来自支持的网络框架，扩展名为如下：

    - *.caffemodel (Caffe,http://caffe.berkeleyvision.org/)
    - *.pb (TensorFlow, https://www.tensorflow.org/)
    - *.t7 | *.net (Torch, http://torch.ch/)
    - *.weights (Darknet, https://pjreddie.com/darknet/)
    - *.bin (DLDT, https://software.intel.com/openvino-toolkit)

- config针对模型二进制的描述文件，不同的框架配置文件有不同扩展名：

    - *.prototxt (Caffe, http://caffe.berkeleyvision.org/)
    - *.pbtxt (TensorFlow, https://www.tensorflow.org/)
    - *.cfg (Darknet, https://pjreddie.com/darknet/)
    - *.xml (DLDT, https://software.intel.com/openvino-toolkit)

- framework显示声明参数，说明模型使用哪个框架训练出来的。

### 代码
```python
import cv2
import numpy as np

bin_model = "bvlc_googlenet.caffemodel"
protxt = "bvlc_googlenet.prototxt"

# load CNN model
net = cv2.dnn.readNet(bin_model, protxt)

# 获取各层信息
layer_names = net.getLayerNames()

for name in layer_names:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id : %d, type : %s, name: %s"%(id, layer.type, layer.name))

print("successfully")
```
>输出
```
layer id : 1, type : Convolution, name: conv1/7x7_s2
layer id : 2, type : ReLU, name: conv1/relu_7x7
layer id : 3, type : Pooling, name: pool1/3x3_s2
layer id : 4, type : LRN, name: pool1/norm1
layer id : 5, type : Convolution, name: conv2/3x3_reduce
layer id : 6, type : ReLU, name: conv2/relu_3x3_reduce
layer id : 7, type : Convolution, name: conv2/3x3
layer id : 8, type : ReLU, name: conv2/relu_3x3
layer id : 9, type : LRN, name: conv2/norm2
layer id : 10, type : Pooling, name: pool2/3x3_s2
...
successfully
```