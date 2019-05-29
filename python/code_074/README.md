#### 二值图像分析 – 提取最大轮廓与编码关键点

1. 二值化处理
```python
# src = cv.GaussianBlur(src, (5, 5), 0)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, se)
```

2. 寻找最大面积的轮廓
```python
# 轮廓提取
out, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
index = 0
max = 0
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    if h >=height or w >= width:
        continue
    area = cv.contourArea(contours[c])
    if area > max:
        max = area
        index = c
```
3. 输出

<img src=result.png width=300>
<img src=output.png width=300>
