#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date:   2019-09-19 18:13:22

@author: JimmyHua
"""

import numpy as np
import cv2 as cv

# 读取数据
img = cv.imread('../code_114/digits.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
x = np.array(cells)

# 创建训练与测试数据
train = x[:,:50].reshape(-1,400).astype(np.float32)    # Size = (2500,400)
test = x[:,50:100].reshape(-1,400).astype(np.float32)  # Size = (2500,400)
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]


# 保存训练数据
np.savez('knn_data.npz',train=train, train_labels=train_labels)

test_labels = train_labels.copy()

# 加载训练数据
with np.load('knn_data.npz') as data:
  print( data.files )
  train = data['train']
  train_labels = data['train_labels']

# 初始化KNN，并训练
knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)

# 计算准确率
matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print(accuracy)


 

