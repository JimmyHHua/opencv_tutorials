import cv2 as cv

box = cv.imread("D:/vcprojects/data/box.png");
box_in_sence = cv.imread("D:/vcprojects/data/box_in_scene.png");
cv.imshow("box", box)
cv.imshow("box_in_sence", box_in_sence)

# 创建ORB特征检测器
sift = cv.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(box,None)
kp2, des2 = sift.detectAndCompute(box_in_sence,None)

# 暴力匹配
bf = cv.DescriptorMatcher_create(cv.DescriptorMatcher_BRUTEFORCE)
matches = bf.match(des1,des2)

# 绘制匹配
matches = sorted(matches, key = lambda x:x.distance)
result = cv.drawMatches(box, kp1, box_in_sence, kp2, matches[:15], None)
cv.imshow("orb-match", result)
cv.imwrite("orb-match.jpg", result)
cv.waitKey(0)
cv.destroyAllWindows()


