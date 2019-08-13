### 特征提取之关键点检测 - GFTTDetector

该方法是基于shi-tomas角点检测变化而来的一种特征提取方法，OpenCV创建该检测器的API与goodfeaturetotrack的API参数极其类似：
```
Ptr<GFTTDetector> cv::GFTTDetector::create(
	int maxCorners = 1000,
	double qualityLevel = 0.01,
	double minDistance = 1,
	int blockSize = 3,
	bool useHarrisDetector = false,
	double k = 0.04
)
```
唯一不同的，该方法返回一个指针。

PS:
>需要注意的是该方法无法提取描述子，只支持提取关键点！

**代码：**

```python
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
```

![](GFTT-Keypoint-Detect.jpg)
