# OpenCV 4.0 Tutorial
[![](https://img.shields.io/badge/opencv-v4.0.0-orange.svg)](https://opencv.org/)       [![](https://img.shields.io/badge/opencv-tutorial-brightgreen.svg)](https://docs.opencv.org/4.0.0/d9/df8/tutorial_root.html)
## Introduction

This repository contains source code of OpenCV Tutorial application, the environment is python3.0 and opencv4.0.

## Sample
- Image load
```python
import cv2

src = cv2.imread("test.png")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- Gray Image
```python
gray = cv2.cvtColor(src, cv.COLOR_BGR2GRAY)
```
---
**More opencv4.0 tutorials plese follow the learning road as below** 👇👇👇

## Learning Road ⛳️
- ✔️ : **Basic**
- ✏️ : **Attention**
- ❣️ : **Important**

No    | Description   | Annotation
:--------: | :--------: | :--------:
code_001 | [图片读取与显示](python/code_001/opencv_001.py)   | ✔️
code_002 | [图片灰度化](python/code_002/opencv_002.py)   | ✔️
code_003 | [图像创建与赋值](python/code_003/opencv_003.py)   | ✔️
code_004 | [图像像素读写](python/code_004/opencv_004.py)   | ✔️
code_005 | [图像像素算术操作(加减乘除)](python/code_005/opencv_005.py)   | ✔️
code_006 | [图像伪彩色增强](python/code_006/opencv_006.py)   | ✔️
code_007 | [图像像素操作(逻辑操作)](python/code_007/opencv_007.py)   | ✔️
code_008 | [图像通道分离合并](python/code_008/opencv_008.py)   | ✔️
code_009 | [色彩空间与色彩空间转换](python/code_009/opencv_009.py)   | ✏️
code_010 | [图像像素值统计](python/code_010/opencv_010.py)   | ✔️
code_011 | [图像像素归一化](python/code_011/opencv_011.py)   | ✔️
code_012 | [视频读写](python/code_012/opencv_012.py)   | ✔️
code_013 | [图像翻转](python/code_013/opencv_013.py)   | ✔️
code_014 | [图像插值](python/code_014/opencv_014.py)   | ✔️
code_015 | [绘制几何形状](python/code_015/opencv_015.py)   | ✔️
code_016 | [图像ROI与ROI操作](python/code_016/opencv_016.py)   | ✔️
code_017 | [图像直方图](python/code_017/opencv_017.py)   | ✔️
code_018 | [图像直方图均衡化](python/code_018/opencv_018.py)   | ✏️
code_019 | [图像直方图比较](python/code_019/opencv_019.py)   | ✔️
code_020 | [图像直方图反向投影](python/code_020/opencv_020.py)   | ✔️
code_021 | [图像卷积操作](python/code_021/opencv_021.py)   | ✔️
code_022 | [图像均值与高斯模糊](python/code_022/opencv_022.py)   | ❣️
code_023 | [中值模糊](python/code_023/opencv_023.py)   | ✔️
code_024 | [图像噪声](python/code_024/opencv_024.py)   | ✔️
code_025 | [图像去噪声](python/code_025/opencv_025.py)   | ✔️
code_026 | [高斯双边模糊](python/code_026/opencv_026.py)   | ✔️
code_027 | [均值迁移模糊(mean-shift blur)](python/code_027/opencv_027.py)   | ✔️
code_028 | [图像积分图算法](python/code_028/opencv_028.py)   | ✔️
code_029 | [快速的图像边缘滤波算法](python/code_029/opencv_029.py)   | ✔️
code_030 | [自定义滤波器](python/code_030/opencv_030.py)   | ✔️
code_031 | [Sobel算子](python/code_031/opencv_031.py)   | ✔️
code_032 | [更多梯度算子](python/code_032/opencv_032.py)   | ✔️
code_033 | [拉普拉斯算子(二阶导数算子)](python/code_033/opencv_033.py)   | ✔️
code_034 | [图像锐化](python/code_034/opencv_034.py)   | ✔️
code_035 | [USM 锐化增强算法](python/code_035/opencv_035.py)   | ✔️
code_036 | [Canny边缘检测器](python/code_036/opencv_036.py)   | ❣️
code_037 | [图像金字塔](python/code_037/opencv_037.py)   | ✔️
code_038 | [拉普拉斯金字塔](python/code_038/opencv_038.py)   | ✔️
code_039 | [图像模板匹配](python/code_039/opencv_039.py)   | ✔️
code_040 | [二值图像介绍](python/code_040/opencv_040.py)   | ✔️
code_041 | [基本阈值操作](python/code_041/opencv_041.py)   | ✔️
code_042 | [图像二值寻找法OTSU](python/code_042/opencv_042.py)   | ✏️
code_043 | [图像二值寻找法TRIANGLE](python/code_043/opencv_043.py)   | ✔️
code_044 | [图像自适应阈值算法](python/code_044/opencv_044.py)   | ✏️
code_045 | [图像二值与去噪](python/code_045/opencv_045.py)   | ✏️
code_046 | [图像连通组件寻找](python/code_046/opencv_046.py)   | ✔️
code_047 | [图像连通组件状态统计](python/code_047/opencv_047.py)   | ✔️
code_048 | [轮廓寻找](python/code_048/opencv_048.py)   | ❣️
code_049 | [轮廓外接矩形](python/code_049/opencv_049.py)   | ❣️
code_050 | [轮廓矩形面积与弧长](python/code_050/opencv_050.py)   | ✏️
code_051 | [轮廓逼近](python/code_051/opencv_051.py)   | ✔️
code_052 | [几何矩计算中心](python/code_052/opencv_052.py)   | ✔️
code_053 | [使用Hu矩阵实现轮廓匹配](python/code_053/opencv_053.py)   | ✔️
code_054 | [轮廓圆与椭圆拟合](python/code_054/opencv_054.py)   | ✔️
code_055 | [凸包检测](python/code_055/opencv_055.py)   | ✏️
code_056 | [直线拟合与极值点寻找](python/code_056/opencv_056.py)   | ✔️
code_057 | [点多边形测试](python/code_057/opencv_057.py)   | ✔️
code_058 | [寻找最大内接圆](python/code_058/opencv_058.py)   | ✔️
code_059 | [霍夫曼直线检测](python/code_059/opencv_059.py)   | ✔️
code_060 | [概率霍夫曼直线检测](python/code_060/opencv_060.py)   | ❣️
code_061 | [霍夫曼圆检测](python/code_061/opencv_061.py)   | ❣️
code_062 | [膨胀和腐蚀](python/code_062/opencv_062.py)   | ❣️
code_063 | [结构元素](python/code_063/opencv_063.py)   | ✔️
code_064 | [开运算](python/code_064/opencv_064.py)   | ✏️
code_065 | [闭运算](python/code_065/opencv_065.py)   | ✏️
