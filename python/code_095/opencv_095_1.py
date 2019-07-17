#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date:   2019-07-17 15:40:17

@author: JimmyHua
"""

import cv2 as cv

box = cv.imread("D:/vcprojects/data/box.png",0);
box_in_sence = cv.imread("D:/vcprojects/data/box_in_scene.png",0);
cv.imshow("box", box)
cv.imshow("box_in_sence", box_in_sence)

# 创建ORB特征检测器
orb = cv.ORB_create()

kp1, des1 = orb.detectAndCompute(box,None)
kp2, des2 = orb.detectAndCompute(box_in_sence,None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# knn match
matches = bf.knnMatch(des1, des2, k=1)

# 删除matches里面的空list，并且根据距离排序
while [] in matches:
    matches.remove([])
matches = sorted(matches, key = lambda x:x[0].distance)

# 画出距离最短的前15个点
result = cv.drawMatchesKnn(box, kp1, box_in_sence, kp2, matches[0:15], None, matchColor = (0,255,0), singlePointColor = (255,0,255))
cv.imshow("orb-match", result)
cv.imwrite("orb-match-1.jpg", result)
cv.waitKey(0)
cv.destroyAllWindows()


