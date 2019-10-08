# 图像均值漂移

## 概述

✔️ MeanShfit 均值漂移算法是一种通用的聚类算法，通常可以实现彩色图像分割。

**基本原理**

✔️ 对于给定的一定数量样本，任选其中一个样本，以该样本为中心点划定一个圆形区域，求取该圆形区域内样本的质心，即密度最大处的点，再以该点为中心继续执行上述迭代过程，直至最终收敛。

**彩色图像分割**

✔️ 均值迁移可以不断分割找到空间颜色分布的峰值，然后根据峰值进行相似度合并，解决过度分割问题，得到最终的分割图像，对于图像多维度数据颜色值(RGB)与空间位置(x,y)，所以需要两个窗口半径，一个是空间半径、另外一个是颜色半径，经过均值漂移窗口的所有的像素点会具有相同的像素值。

> 严格来说并不是图像的分割，而是图像在色彩层面的平滑滤波，它可以中和色彩分布相近的颜色，平滑色彩细节，侵蚀掉面积较小的颜色区域。

## 函数

```
dst = cv.pyrMeanShiftFiltering(src, sp, sr, maxLevel, termcrit)
```
其中：
- src --> 输入图像;
- dst --> 输出结果;
- sp --> 表示空间窗口大小;
- sr --> 表示表示颜色空间;
- maxLevel --> 表示金字塔层数，总层数为maxlevel+1;
- termcrit --> 表示停止条件;

## 代码示例

```python
import cv2 as cv
import numpy as np

src = cv.imread("master.jpg")
dst = cv.pyrMeanShiftFiltering(src, 25, 40, None, 2)
cv.imshow("result", np.hstack((src,dst)))
```
<img src=https://i.loli.net/2019/09/20/s9MjNbZPvnDhHeg.jpg width=350>
