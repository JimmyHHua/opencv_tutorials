# Grabcut图像分割

## 概述

✔️ Grabcut是基于图割(graph cut)实现的图像分割算法，它需要用户输入一个bounding box作为分割目标位置，实现对目标与背景的分离/分割。

✔️ Grabcut分割速度快，效果好，支持交互操作，因此在很多APP图像分割/背景虚化的软件中经常使用。

**算法流程**

- 在图片中定义含有（一个或多个）物体的矩形；
- 矩形外的区域被自动认为是背景；
- 对于用户定义的矩形区域，可用背景中数据来区分是前景还是背景；
- 用高斯混合模型（GMM）来对被禁和前景见面，并将未定义的像素标记为可能的前景或背景；
- 图像中的每一个像素都被看作通过通过虚拟变与周围像素连接，而每条边都有一个属于前景或背景的概率这基于它和周围像素颜色上的相似性；
- 每一个像素（即算法中的节点）会与前一各前景或背景节点连接；
- 在节点连接完成后，用图论中最大流最小割的方法来分割。

## 函数

```python
cv2.grabCut(img, rect, mask,
            bgdModel, fgdModel, 
            iterCount, mode = GC_EVAL)
```
其中
- img --> 输入的三通道图像；
- mask --> 输入的单通道图像，初始化方式为GC_INIT_WITH_RECT表示ROI区域可以被初始化为：
    - GC_BGD --> 定义为明显的背景像素 0
    - GC_FGD --> 定义为明显的前景像素 1
    - GC_PR_BGD --> 定义为可能的背景像素 2
    - GC_PR_FGD --> 定义为可能的前景像素 3
- rect --> 表示roi区域；
- bgdModel --> 表示临时背景模型数组；
- fgdModel --> 表示临时前景模型数组；
- iterCount --> 表示图割算法迭代次数, 次数越多，效果越好；
- mode --> 当使用用户提供的roi时候使用GC_INIT_WITH_RECT。

## 示例代码

```
import cv2 as cv
import numpy as np

src = cv.imread("m1.jpg")
src = cv.resize(src, (0,0), fx=0.5, fy=0.5)
r = cv.selectROI('input', src, False)  # 返回 (x_min, y_min, w, h)

# roi区域
roi = src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# 原图mask
mask = np.zeros(src.shape[:2], dtype=np.uint8)

# 矩形roi
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3])) # 包括前景的矩形，格式为(x,y,w,h)

bgdmodel = np.zeros((1,65),np.float64) # bg模型的临时数组
fgdmodel = np.zeros((1,65),np.float64) # fg模型的临时数组

cv.grabCut(src,mask,rect,bgdmodel,fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)

# 提取前景和可能的前景区域
mask2 = np.where((mask==1) + (mask==3), 255, 0).astype('uint8')

print(mask2.shape)

result = cv.bitwise_and(src,src,mask=mask2)
cv.imwrite('result.jpg', result)
cv.imwrite('roi.jpg', roi)

cv.imshow('roi', roi)
cv.imshow("result", result)
cv.waitKey(0)
cv.destroyAllWindows()
```

输入：

采用 selectROI, 可以在图中自己选定ROI区域：
- 选定后，按enter 或则 Space 进行grabcut；
- 重新选ROI，只需用鼠标重新选择即可；
- 按 c 结束程序。

1）显示原图：

<img src=https://i.loli.net/2019/09/20/UyJQqzXd7bwfg1u.jpg>


2）选择ROI：

<img src=https://i.loli.net/2019/09/20/muQ1S62YtLfUjkT.jpg>

3）输出结果:

<img src= https://i.loli.net/2019/09/20/5F1w7pY6mPDWock.jpg>