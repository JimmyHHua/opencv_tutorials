# OpenCV 4.0 Tutorial
[![](https://img.shields.io/badge/opencv-v4.0.0-orange.svg)](https://opencv.org/)       [![](https://img.shields.io/badge/opencv-tutorial-brightgreen.svg)](https://docs.opencv.org/4.0.0/d9/df8/tutorial_root.html)
## 简介

这个库包含OpenCV教程应用程序的源代码，运行环境是python3 和 opencv4.0(v4.1也可以)。

## 样例

- **图片读取**

```python
import cv2

src = cv2.imread("test.png")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
<div align=center><img src="https://i.loli.net/2019/05/22/5ce4b40258c9155103.jpg" width=200></div>

- **灰度图**
```python
gray = cv2.cvtColor(src, cv.COLOR_BGR2GRAY)
```
<div align=center><img src=https://i.loli.net/2019/05/22/5ce4b2ae1e7ce86434.png width=120>       <img src=https://i.loli.net/2019/05/22/5ce4b2ae220a248459.png width=120></div>


**更多的opencv教程请参考下面的学习路径** 👇👇👇

## 学习路径 ⛳️

***备注:***

- ✔️ : **基础**
- ✏️ : **值得注意**
- ❣️ : **重要知识点**

序号    | 描述   | 备注
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
code_066 | [开闭运算的应用](python/code_066/opencv_066.py)   | ✏️
code_067 | [顶帽](python/code_067/opencv_067.py)   | ✔️
code_068 | [黑帽](python/code_068/opencv_068.py)   | ✔️
code_069 | [图像梯度](python/code_069/opencv_069.py)   | ✔️
code_070 | [基于梯度的轮廓发现](python/code_070/opencv_070.py)   | ✏️
code_071 | [击中击不中](python/code_071/opencv_071.py)   | ✔️
code_072 | [缺陷检测1](python/code_072)   | ✔️
code_073 | [缺陷检测2](python/code_073/opencv_073.py)   | ✔️
code_074 | [提取最大轮廓和编码关键点](python/code_074)   | ✔️
code_075 | [图像修复](python/code_075/opencv_075.py)   | ✔️
code_076 | [图像透视变换应用](python/code_076/opencv_076.py)   | ✏️
code_077 | [视频读写和处理](python/code_077/opencv_077.py)   | ✏️
code_078 | [识别与跟踪视频中的特定颜色对象](python/code_078)   | ✔️
code_079 | [视频分析-背景/前景 提取](python/code_079/opencv_079.py)   | ✔️
code_080 | [视频分析–背景消除与前景ROI提取](python/code_080)   | ✔️
code_081 | [角点检测-Harris角点检测](python/code_081)   | ✔️
code_082 | [角点检测-Shi-Tomas角点检测](python/code_082)   | ✏️
code_083 | [角点检测-亚像素角点检测](python/code_083)   | ✔️
code_084 | [视频分析-KLT光流跟踪算法-1](python/code_084)   | ✏️
code_085 | [视频分析-KLT光流跟踪算法-2](python/code_085)   | ✏️
code_086 | [视频分析-稠密光流分析](python/code_086)   | ✏️
code_087 | [视频分析-帧差移动对象分析](python/code_087/opencv_087.py)   | ✔️
code_088 | [视频分析-均值迁移](python/code_088)   | ✏️
code_089 | [视频分析-连续自适应均值迁移](python/code_089)   | ✏️
code_090 | [视频分析-对象移动轨迹绘制](python/code_090)   | ✔️
code_091 | [对象检测-HAAR级联分类器](python/code_091)   | ✔️
code_092 | [对象检测-HAAR特征分析](python/code_092)   | ✔️
code_093 | [对象检测-LBP特征分析](python/code_093/opencv_093.py)   | ✔️
code_094 | [ORB 特征关键点检测](python/code_094)   | ✏️
code_095 | [ORB 特征描述子匹配](python/code_095)   | ✔️
code_096 | [多种描述子匹配方法](python/code_096)   | ✏️
code_097 | [基于描述子匹配的已知对象定位](python/code_097)   | ✏️
code_098 | [SIFT 特征关键点检测](python/code_097)   | ✔️
code_099 | [SIFT 特征描述子匹配](python/code_097)   | ✔️
code_100 | [HOG 行人检测](python/code_100/opencv_100.py)   | ✔️
code_101 | [HOG 多尺度检测](python/code_101/opencv_101.py)   | ✏️
code_102 | [HOG 提取描述子](python/code_102/opencv_102.py)   | ✔️
code_103 | [HOG 使用描述子生成样本数据](python/code_103/opencv_103.py)   | ✔️
code_104 | [(检测案例)-HOG+SVM 训练](python/code_104/opencv_104.py)   | ✔️
code_105 | [(检测案例)-HOG+SVM 预测](python/code_105/opencv_105.py)   | ✔️
code_106 | [AKAZE 特征与描述子](python/code_106)   | ✔️
code_107 | [Brisk 特征与描述子](python/code_107)   | ✔️
code_108 | [GFTT关键点检测](python/code_108)   | ✔️
code_109 | [BLOB 特征分析](python/code_109)   | ✔️
code_110 | [KMeans 数据分类](python/code_110)   | ✔️
code_111 | [KMeans 图像分割](python/code_111)   | ✔️
code_112 | [KMeans 图像替换](python/code_112)   | ✔️
code_113 | [KMeans 图像色卡提取](python/code_113)   | ✔️
code_114 | [KNN 分类模型](python/code_114)   | ✔️
code_115 | [KNN 数据保存](python/code_115)   | ✔️
code_116 | [决策树算法](python/code_116)   | ✔️
code_117 | [图像均值漂移分割](python/code_117)   | ✔️
code_118 | [Grabcut-图像分割](python/code_118)   | ✔️
code_119 | [Grabcut-背景替换](python/code_119)   | ✏️
code_120 | [二维码检测识别](python/code_120)   | ✔️
code_121 | [DNN- 读取模型各层信息](python/code_121)   | ✔️
code_122 | [DNN- DNN实现图像分类](python/code_122)   | ✔️
code_123 | [DNN- 模型运行设置目标设备与计算后台](python/code_123)   | ✔️
code_124 | [DNN- SSD单张图片检测](python/code_124)   | ✔️
code_125 | [DNN- SSD实时视频检测](python/code_125)   | ✔️
code_126 | [DNN- 基于残差网络的人脸检测](python/code_126)   | ✔️
code_127 | [DNN- 基于残差网络的视频人脸检测](python/code_127)   | ✔️
code_128 | [DNN- 调用tensorflow的检测模型](python/code_128)   | ✔️
code_129 | [DNN- 调用openpose模型实现姿态评估](python/code_129)   | ✔️
code_130 | [DNN- 调用YOLO对象检测网络](python/code_130)   | ✔️
code_131 | [DNN- YOLOv3-tiny版本实时对象检测](python/code_131)   | ✔️
code_132 | [DNN- 单张与多张图像的推断](python/code_132)   | ✔️
code_133 | [DNN- 图像颜色化模型使用 ](python/code_133)   | ✔️
code_134 | [DNN- ENet实现图像分割](python/code_134)   | ✔️
code_135 | [DNN- 实时快速的图像风格迁移](python/code_135)   | ✔️

---

### 附录

⛳️ DNN模块的一些模型下载可以从下面的谷歌云中获取：

🌱 [Weight for DNN](https://drive.google.com/drive/folders/1mg6VXpkvEmyL1scaelX5FnW8uw1gk9iq?usp=sharing)