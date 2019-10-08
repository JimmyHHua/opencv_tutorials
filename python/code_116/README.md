# Opencv 决策树算法

 ✔️ OpenCV中机器学习模块的决策树算法分为两个类别：
 
-  一个是随机森林(Random Trees)
-  强化分类(Boosting Classification)

Opencv的函数使用方法和前面的KNN一样，都是通过`cv2.ml` 创建。

eg. 随机森林

```python
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
```
输出：
```
data loading...
acc is :  83.72
```