import cv2 as cv
import numpy as np


def laplaian_demo(pyramid_images):
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            h, w = src.shape[:2]
            expand = cv.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv.subtract(src, expand) + 127
            cv.imshow("lpls_" + str(i), lpls)
        else:
            h, w = pyramid_images[i-1].shape[:2]
            expand = cv.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv.subtract(pyramid_images[i-1], expand) + 127
            cv.imshow("lpls_"+str(i), lpls)


def pyramid_up(image, level=3):
    temp = image.copy()
    # cv.imshow("input", image)
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        # cv.imshow("pyramid_up_" + str(i), dst)
        temp = dst.copy()
    return pyramid_images


src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
# pyramid_up(src)
laplaian_demo(pyramid_up(src))

cv.waitKey(0)
cv.destroyAllWindows()

