import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 克隆图像
m1 = np.copy(src)

# 赋值
m2 = src
src[100:200,200:300,:] = 255
cv.imshow("m2",m2)

m3 = np.zeros(src.shape, src.dtype)
cv.imshow("m3", m3)

m4 = np.zeros([512,512], np.uint8)
# m4[:,:] =127 try to give gray value 127
cv.imshow("m4", m4)

m5 = np.ones(shape=[512,512,3], dtype=np.uint8)
m5[:,:,0] = 255
cv.imshow("m5", m5)




cv.waitKey(0)
cv.destroyAllWindows()

