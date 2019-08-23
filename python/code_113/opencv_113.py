import numpy as np
import cv2 as cv

image = cv.imread('result1.jpg')
image2 = cv.imread('result2.jpg')
img = cv.resize(image,(300,510))
img2 = cv.resize(image2,(300,510))
cv.imshow("input", img)
cv.imwrite('result1_1.jpg',img)
cv.imwrite('result2_2.jpg',img2)
# h, w ,ch = image.shape
# print(image.shape)
# # 构建图像数据
# data = image.reshape((-1,3))
# data = np.float32(data)

# # 图像分割
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# num_clusters = 5
# ret,label,center=cv.kmeans(data, num_clusters, None, criteria, num_clusters, cv.KMEANS_RANDOM_CENTERS)
# print(label[300])

# # 生成主色彩条形卡片
# card = np.zeros((50, w, 3), dtype=np.uint8)
# clusters = np.zeros([5], dtype=np.int32)
# # 统计每一类的数目
# for i in range(len(label)):
#     clusters[label[i]] += 1
# # 比重
# clusters = np.float32(clusters) / float(h*w)
# center = np.int32(center)
# x_offset = 0

# # 绘制色卡
# for c in range(num_clusters):
#     dx = np.int(clusters[c] * w)
#     b = center[c][0]
#     g = center[c][1]
#     r = center[c][2]
#     cv.rectangle(card, (x_offset, 0), (x_offset+dx, 50), (int(b), int(g), int(r)), -1)
#     x_offset += dx

# cv.imshow("color table", card)
cv.waitKey(0)
cv.destroyAllWindows()