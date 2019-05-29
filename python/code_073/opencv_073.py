import cv2 as cv
import numpy as np

def get_template(binary, boxes):
    x, y, w, h = boxes[0]
    roi = binary[y:y+h, x:x+w]
    return roi


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


src = cv.imread("ce_02.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 图像二值化
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_OPEN, se)
cv.imshow("binary", binary)

# 轮廓提取
out, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
rects = []
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    area = cv.contourArea(contours[c])
    if h > (height//2):
        continue
    if area < 150:
        continue
    rects.append([x, y, w, h])

# 排序轮廓
rects = sorted(rects, key = lambda x:x[1])
print(rects)
template = get_template(binary, rects);

# 填充边缘
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    area = cv.contourArea(contours[c])
    if h > (height//2):
        continue
    if area < 150:
        continue
    cv.drawContours(binary, contours, c, (0), 2, 8)
cv.imshow("template", template)

# 检测缺陷
defect_boxes = detect_defect(binary, rects, template)
for dx, dy, dw, dh in defect_boxes:
    cv.rectangle(src, (dx, dy), (dx + dw, dy + dh), (0, 0, 255), 1, 8, 0)
    cv.putText(src, "bad", (dx, dy-2), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 2)

index = 1
for dx, dy, dw, dh in rects:
    cv.putText(src, "num:%d"%index, (dx-52, dy+30), cv.FONT_HERSHEY_SIMPLEX, .5, (30, 122, 233), 2)
    index += 1

cv.imshow("result", src)
cv.imwrite("binary2.png", src)

cv.waitKey(0)
cv.destroyAllWindows()