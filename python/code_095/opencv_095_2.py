#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date:   2019-07-17 15:27:36

@author: JimmyHua
"""

import cv2 as cv

box = cv.imread("D:/vcprojects/data/box.png",0);
box_in_sence = cv.imread("D:/vcprojects/data/box_in_scene.png",0);
cv.imshow("box", box)
cv.imshow("box_in_sence", box_in_sence)

# 创建ORB特征检测器
orb = cv.xfeatures2d.SIFT_create()

kp1, des1 = orb.detectAndCompute(box,None)
kp2, des2 = orb.detectAndCompute(box_in_sence,None)


index_params = dict(algorithm = 0, trees = 5)

search_params = dict(checks=20)

flann = cv.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1, des2, k=2)
print(matches[0:5])

# 记录好的点
goodMatches = [[0,0] for i in range(len(matches))]

for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        goodMatches[i]=[1,0]

draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0), matchesMask = goodMatches, flags = 0)

result = cv.drawMatchesKnn(box, kp1, box_in_sence, kp2, matches, None, **draw_params)

cv.imshow("orb-match", result)
cv.imwrite("orb-match-2.jpg", result)
cv.waitKey(0)
cv.destroyAllWindows()


