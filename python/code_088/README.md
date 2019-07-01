# 基于均值迁移的对象移动分析(Meanshift)
✏️ ⛳️👍

## 概述

**本质：**

✔️ Mean Shift均值漂移算法是无参密度估计理论的一种，无参密度估计不需要事先知道对象的任何先验知识，完全依靠训练数据进行估计，并且可以用于任意形状的密度估计，在某一连续点处的密度函数值可由该点邻域中的若干样本点估计得出。

**直观的理解：**

✔️ 一堆点集，一个圆形的窗口在不断的移动，移动的方向是沿着点的密度最大的区域移动，图示如下：

<img src="https://i.loli.net/2019/07/01/5d19bd30b369945214.jpg" alt="meanshift.jpg" title="meanshift.jpg" width=400/>


## 函数

- 在OpenCV里使用均值平移，首先需要设置目标，找到它的直方图，这样我们可以为了计算均值平移向后投影目标到每一帧上，同时也需要提供窗口的初始位置。

- 对于直方图，只考虑色调(H)，要避免低光线带来的错误值，低光线的值使用 `cv2.inRange()` 函数来丢弃掉。

```
ret, track_window = cv2.meanShift(probImage, window, criteria )
```
> 输入值
- probImage --> 输入图像，是直方图反向投影的结果
- window --> 搜索窗口，ROI对象区域
- criteria --> 均值迁移停止条件

> 返回值
- ret --> 返回迭代次数
- track_window --> 返回迭代后的窗口


<img src="https://i.loli.net/2019/06/28/5d15ef132bd0239773.gif" alt="ss.gif" title="ss.gif" width= 400/>
