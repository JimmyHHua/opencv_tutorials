import cv2 as cv
import numpy as np

src = cv.imread("master.jpg")
dst = cv.pyrMeanShiftFiltering(src, 25, 40, None, 2)
cv.imshow("result", np.hstack((src,dst)))
cv.imwrite("result.jpg", np.hstack((src,dst)))
cv.waitKey(0)
cv.destroyAllWindows()