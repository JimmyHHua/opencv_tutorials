#### 二值图像分析 – 缺陷检测

1. 观察图像与提取图像ROI对象轮廓外接矩形与轮廓.
```python
# Get contours
_, contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    area = cv.contourArea(contours[c])
    if h > (height//2):
        continue
    if area < 150:
        continue
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)
    cv.drawContours(src, contours, c, (0, 255, 0), 2, 8)
```
<img src=ce_02.jpg width=300>
<img src=binary2.png width=300>

2. 对于得到的刀片外接矩形，首先需要通过排序，确定他们的编号.

👀 [代码Code](../code_073/opencv_073.py)

```
# 排序轮廓
rects = sorted(rects, key = lambda x:x[1])
```
3. 根据模板进行相减得到与模板不同的区域，对这些区域进行形态学操作，去掉边缘细微差异，最终就得到了可以检出的缺陷或者划痕刀片。

```python
# 获取模板
def get_template(binary, boxes):
    x, y, w, h = boxes[0]
    roi = binary[y:y+h, x:x+w]
    return roi

# 缺陷检测函数
def detect_defect(binary, boxes, tpl):
    height, width = tpl.shape
    index = 1
    defect_rois = []
    # 发现缺失
    for x, y, w, h in boxes:
        roi = binary[y:y + h, x:x + w]
        roi = cv.resize(roi, (width, height))
        mask = cv.subtract(tpl, roi)
        se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, se)
        ret, mask = cv.threshold(mask, 0, 255, cv.THRESH_BINARY)
        count = 0
        for row in range(height):
            for col in range(width):
                pv = mask[row, col]
                if pv == 255:
                    count += 1
        if count > 0:
            defect_rois.append([x, y, w, h])
        cv.imwrite("mask%d.png"%index, mask)
        index += 1
    return defect_rois

```

<img src=../code_073/ce_02.jpg width=300>
<img src=../code_073/binary2.png width=300>
