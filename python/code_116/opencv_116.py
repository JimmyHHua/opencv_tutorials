import numpy as np
import cv2 as cv
from sklearn import metrics

# 读取数据
img = cv.imread('../code_114/digits.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
x = np.array(cells)
print('data loading...')

# 创建训练与测试数据
train = x[:,:50].reshape(-1,400).astype(np.float32)
test = x[:,50:100].reshape(-1,400).astype(np.float32)
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()

# 训练随机树
dt = cv.ml.RTrees_create()
dt.train(train, cv.ml.ROW_SAMPLE, train_labels)
retval, results = dt.predict(test)

# 计算准确率
matches = results==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/results.size
print('acc is : ', accuracy)