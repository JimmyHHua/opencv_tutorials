import cv2 as cv
import numpy as np

# load image
frame = cv.imread("zhifang_ball.png")
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
params = cv.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0;
params.maxThreshold = 256;

# Filter by Area.
params.filterByArea = True
params.minArea = 100

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.5

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.5

detector = cv.SimpleBlobDetector_create(params)

# Detect blobs.
cv.imshow("input", frame)
keypoints = detector.detect(gray)
result = cv.drawKeypoints(frame, keypoints, None, (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("result", result)
cv.imwrite("result.png", result)
cv.waitKey(0)
cv.destroyAllWindows()