## OpenCV DNN 支持YOLOv3-tiny版本实时对象检测


YOLOv3的模型在CPU上无法做到实时运行，而YOLO作者提供了个YOLOv3版本的精简版对象检测模型，大小只有30MB左右，它可以在CPU上做到实时运行，这个模型就是YOLOv3-tiny模型。

相比YOLOv3，YOLOv3-tiny只有两个输出层，而且权重参数层与参数文件大小都大大的下降，可以在嵌入式设备与前端实时运行。
