import cv2 as cv

box = cv.imread("D:/vcprojects/data/box.png");
box_in_sence = cv.imread("D:/vcprojects/data/box_in_scene.png");
cv.imshow("box", box)
cv.imshow("box_in_sence", box_in_sence)

# 创建ORB特征检测器
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(box,None)
kp2, des2 = orb.detectAndCompute(box_in_sence,None)

# 暴力匹配，汉明距离匹配特征点
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

# 绘制匹配，只提取距离最小的10个点
matches = sorted(matches, key = lambda x:x.distance)
result = cv.drawMatches(box, kp1, box_in_sence, kp2, matches[:10], None)
cv.imshow("orb-match", result)
cv.imwrite("orb-match.jpg", result)
cv.waitKey(0)
cv.destroyAllWindows()


