import cv2 as cv
import numpy as np


def template_demo():
    src = cv.imread("./test.png")
    tpl = cv.imread("./test01.png")
    cv.imshow("input", src)
    cv.imshow("tpl", tpl)
    th, tw = tpl.shape[:2]
    result = cv.matchTemplate(src, tpl, cv.TM_CCORR_NORMED)
    cv.imshow("result", result)
    cv.imwrite("D:/039_003.png", np.uint8(result*255))
    t = 0.98
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)
    cv.imshow("llk-demo", src)
    cv.imwrite("D:/039_004.png", src)


template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
