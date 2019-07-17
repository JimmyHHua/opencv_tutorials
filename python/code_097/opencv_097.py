#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date:   2019-07-16 16:27:14

@author: JimmyHua
"""

import cv2 as cv
import numpy as np

box = cv.imread("D:/vcprojects/data/box.png");
box_in_sence = cv.imread("D:/vcprojects/data/box_in_scene.png");
cv.imshow("box", box)
cv.imshow("box_in_sence", box_in_sence)

# 创建ORB特征检测器
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(box,None)
kp2, des2 = orb.detectAndCompute(box_in_sence,None)

# 暴力匹配
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
goodMatches = []

# 筛选出好的描述子
matches = sorted(matches, key = lambda x:x.distance)
for i in range(len(matches)):
    if (matches[i].distance < 0.46 * matches[-1].distance):
            goodMatches.append(matches[i])

result = cv.drawMatches(box, kp1, box_in_sence, kp2, goodMatches, None)

obj_pts, scene_pts = [], []

# 单独保存 obj 和 scene 好的点位置
for f in goodMatches:
    obj_pts.append(kp1[f.queryIdx].pt)
    scene_pts.append(kp2[f.trainIdx].pt)

#H, _= cv.findHomography(np.float32(obj_pts), np.float32(scene_pts), cv.RANSAC)

H, _ = cv.findHomography(np.float32(obj_pts), np.float32(scene_pts), cv.RHO)

h, w = box.shape[0:2]

pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
dst = cv.perspectiveTransform(pts, H).reshape(-1, 2)
# 加上偏移量
for i in range(4):
    dst[i][0] += w

cv.polylines(result, [np.int32(dst)], True, (0, 255, 0), 3, cv.LINE_AA)

cv.imshow("orb-match", result)
cv.imwrite("orv-match.jpg", result)

cv.waitKey(0)
cv.destroyAllWindows()
