import cv2 as cv
import numpy as np

src = cv.imread("../code_118/m1.jpg")
src = cv.resize(src, (0,0), fx=0.5, fy=0.5)
r = cv.selectROI('input', src, False)  # 返回 (x_min, y_min, w, h)

# roi区域
roi = src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
img = src.copy()
cv.rectangle(img, (int(r[0]), int(r[1])),(int(r[0])+int(r[2]), int(r[1])+ int(r[3])), (255, 0, 0), 2)

# 原图mask
mask = np.zeros(src.shape[:2], dtype=np.uint8)

# 矩形roi
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3])) # 包括前景的矩形，格式为(x,y,w,h)

bgdmodel = np.zeros((1,65),np.float64) # bg模型的临时数组  13 * iterCount
fgdmodel = np.zeros((1,65),np.float64) # fg模型的临时数组  13 * iterCount

cv.grabCut(src,mask,rect,bgdmodel,fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)

# 提取前景和可能的前景区域
mask2 = np.where((mask==1) + (mask==3), 255, 0).astype('uint8')
background = cv.imread("flower.png")

h, w, ch = src.shape
background = cv.resize(background, (w, h))
cv.imwrite("background.jpg", background)

mask = np.zeros(src.shape[:2], dtype=np.uint8)
bgdmodel = np.zeros((1,65),np.float64)
fgdmodel = np.zeros((1,65),np.float64)

cv.grabCut(src,mask,rect,bgdmodel,fgdmodel,5,mode=cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==1) + (mask==3), 255, 0).astype('uint8')

# 高斯模糊
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
cv.dilate(mask2, se, mask2)
mask2 = cv.GaussianBlur(mask2, (5, 5), 0)
cv.imshow('background-mask',mask2)
cv.imwrite('background-mask.jpg',mask2)


# 虚化背景
background = cv.GaussianBlur(background, (0, 0), 15)
mask2 = mask2/255.0
a =  mask2[..., None]

# 融合方法 com = a*fg + (1-a)*bg
result = a* (src.astype(np.float32)) +(1 - a) * (background.astype(np.float32))


cv.imshow("result", result.astype(np.uint8))
cv.imwrite("result.jpg", result.astype(np.uint8))

cv.waitKey(0)
cv.destroyAllWindows()