#### 视频分析 – 背景消除与前景ROI提取

通过视频中的背景进行建模，实现背景消除，生成mask图像，通过对mask二值图像分析实现对前景活动对象ROI区域的提取，是很多视频监控分析软件常用的手段之一，该方法很实时！整个步骤如下：
1.	初始化背景建模对象GMM
2.	读取视频一帧
3.	使用背景建模消除生成mask
4.	对mask进行轮廓分析提取ROI
5.	绘制ROI对象

函数：

OpenCV中实现的背景模型提取算法有两种，一种是基于高斯混合模型GMM实现的背景提取，另外一种是基于最近邻KNN实现的。都有相关的API可以供开发者使用。
**相关API：**
```
Ptr<BackgroundSubtractorMOG2> cv::createBackgroundSubtractorMOG2(
int  history = 500,
double 	varThreshold = 16,
bool  detectShadows = true
)
```
>参数解释如下：
history表示过往帧数，500帧，选择history = 1就变成两帧差
varThreshold表示像素与模型之间的马氏距离，值越大，只有那些最新的像素会被归到前景，值越小前景对光照越敏感。
detectShadows 是否保留阴影检测，请选择False这样速度快点。

创建
Ptr<BackgroundSubtractor> pBackSub = createBackgroundSubtractorMOG2();
Ptr<BackgroundSubtractor> pBackSub = createBackgroundSubtractorKNN();

```python

# 创建背景提取器
fgbg = cv.createBackgroundSubtractorMOG2(
    history=500, varThreshold=100, detectShadows=False)


def process(image, opt=1):

    # 提取前景mask
    mask = fgbg.apply(frame)
    line = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)
    cv.imshow("mask", mask)
    # 轮廓提取, 发现最大轮廓
    out, contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv.minAreaRect(contours[c])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image, mask


```
<img src=../code_080/input.png width=300>
<img src=../code_080/mask.png width=300>
<img src=../code_080/result.png width=300>
