# 基于连续自适应均值迁移的对象移动分析(Camshift)

## 概述

✔️ 由于mean-shift算法的窗口是固定大小的，而我们需要让窗口大小和目标的大小以及旋转相适应，因此提出了Camshift。

✔️ CAM是连续自适应的均值迁移跟踪算法，它跟均值迁移相比较有两个改进
- 会根据跟踪对象大小变化自动调整搜索窗口大小
- 返回位置信息更加完整，包含了位置与角度信息。

✔️ CAM先采用均值平移，当平移覆盖后，更新窗口大小，公式如下：
```math
s=2 x \sqrt{\frac{M 00}{256}}
```
>它也计算最适合的椭圆的方向，然后它在使用新的大小的窗口在之前的位置开始进行均值平移，过程不断继续直到到达指定的准确率。

## 函数

```
ret, track_box = cv2.CamShift(
                InputArray probImage,
                Rect &  window,
                TermCriteria criteria )
```
>输入
- probImage --> 输入图像，是直方图反向投影的结果
- window --> 搜索窗口，ROI对象区域
- criteria --> 均值迁移停止条件

>输出
- ret --> 返回可变角度的最优外接椭圆
- track_box --> 返回新的窗口


<img src="https://i.loli.net/2019/07/01/5d19c0b1265c267527.gif" alt="ss.gif" title="ss.gif" width=400/>