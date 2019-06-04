#### 识别与跟踪视频中的特定颜色对象

这个是其实图像处理与二值分析的视频版本，通过读取视频每一帧的图像，然后对图像二值分析，得到指定的色块区域，主要步骤如下：
1.	色彩转换BGR2HSV
2.	inRange提取颜色区域mask
3.	对mask区域进行二值分析得到位置与轮廓信息
4.	绘制外接椭圆与中心位置
5.	显示结果

其中涉及到的知识点主要包括图像处理、色彩空间转换、形态学、轮廓分析等。

函数：
```python
def process(image, opt=1):

    # BGR转换为HSV
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    line = cv.getStructuringElement(cv.MORPH_RECT, (15, 15), (-1, -1))

    # Inrange
    mask = cv.inRange(hsv, (0, 43, 46), (10, 255, 255))

    # 开操作，去除吊小的噪点
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)

    # 轮廓提取, 发现最大轮廓
    out, contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    index = -1
    max = 0
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area > max:
            max = area
            index = c
    # 绘制
    if index >= 0:
        rect = cv.minAreaRect(contours[index])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image

```

<img src=../code_078/result.jpg width=300>
