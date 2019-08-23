import numpy as np
import cv2 as cv

image = cv.imread('toux.jpg')
cv.imshow("input", image)
h, w ,ch = image.shape
# 构建图像数据
data = image.reshape((-1,3))
data = np.float32(data)

# 图像分割
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
num_clusters = 4
ret,label,center=cv.kmeans(data, num_clusters, None, criteria, num_clusters, cv.KMEANS_RANDOM_CENTERS)

# 生成mask区域
index = label[0][0]
center = np.uint8(center)
color = center[0]
mask = np.ones((h, w), dtype=np.uint8)*255.
label = np.reshape(label, (h, w))
# alpha图
mask[label == index] = 0

# 高斯模糊
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
# 膨胀，防止背景出现
cv.erode(mask, se, mask)
#边缘模糊
mask = cv.GaussianBlur(mask, (5, 5), 0)
cv.imshow('background-mask',mask)

# 白色背景
bg = np.ones(image.shape, dtype=np.float)*255.

# 粉丝背景
purle = np.array([255, 0, 255])
bg_color = np.tile(purle, (image.shape[0], image.shape[1], 1))

alpha = mask.astype(np.float32) / 255.
fg = alpha[..., None] * image
new_image = fg + (1 - alpha[..., None])*bg
new_image_purle = fg + (1 - alpha[..., None])*bg_color

# # blend image
# result = np.zeros((h, w, ch), dtype=np.uint8)
# for row in range(h):
#     for col in range(w):
#         w1 = mask[row, col] / 255.0
#         b, g, r = image[row, col]
#         b = w1 * 255.0 + b * (1.0 - w1)
#         g = w1 * 0 + g * (1.0 - w1)
#         r = w1 * 255 + r * (1.0 - w1)
#         result[row, col] = (b, g, r)
cv.imshow("background substitution", bg_color.astype(np.uint8))
cv.imwrite("white.jpg", np.hstack((image, new_image.astype(np.uint8))))
cv.imwrite("purle.jpg", np.hstack((image, new_image_purle.astype(np.uint8))))
cv.waitKey(0)
cv.destroyAllWindows()