import cv2 as cv


image = cv.imread("hist_02.jpg");
cv.imshow("input", image)

# 创建GFTT特征检测器
gftt = cv.GFTTDetector_create(100, 0.01,1, 3, False, 0.04)
kp1 = gftt.detect(image,None)
result = cv.drawKeypoints(image, kp1, None, (0, 255, 0), cv.DrawMatchesFlags_DEFAULT)

cv.imshow("GFTT-Keypoint-Detect", result)
cv.imwrite("GFTT-Keypoint-Detect.jpg", result)
cv.waitKey(0)
cv.destroyAllWindows()