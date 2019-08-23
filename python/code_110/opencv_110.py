import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取数据
def loadDataSet(fileName):
    data = []
    with open(fileName) as f:
        for line in f.readlines():
            curLine = line.strip().split("\t")
            fltLine = list(map(float, curLine))  # 转换为float
            data.append(fltLine)
    return np.array(data, dtype=np.float32)

# 导入数据
data = loadDataSet('testSet2.txt')

# 定义停止条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# kmeans计算
ret,label,center=cv2.kmeans(data, 3, None, criteria, 2, cv2.KMEANS_RANDOM_CENTERS)

print(len(label))
print(center)

# 获取不同标签的点
A = data[label.ravel()==0]
B = data[label.ravel()==1]
C = data[label.ravel()==2]

# 可视化
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'purple')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'black', marker = '*')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()
