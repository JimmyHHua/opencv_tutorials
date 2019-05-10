import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo():
    sample = cv.imread("./Mat.png")
    # hist2d_demo(sample)
    target = cv.imread("./test.png")
    # hist2d_demo(target)
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show images
    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("backProjectionDemo", dst)


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    dst = cv.resize(hist, (400, 400))
    cv.imshow("image", image)
    cv.imshow("hist", dst)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()


back_projection_demo()
cv.waitKey(0)

cv.destroyAllWindows()
