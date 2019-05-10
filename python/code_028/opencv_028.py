import cv2 as cv
import numpy as np


def get_block_sum(ii, x1, y1, x2, y2, index):
    tl = ii[y1, x1][index]
    tr = ii[y2, x1][index]
    bl = ii[y1, x2][index]
    br = ii[y2, x2][index]
    s = (br - bl - tr + tl)
    return s


def blur_demo(image, ii):
    h, w, dims = image.shape
    result = np.zeros(image.shape, image.dtype)
    ksize = 15
    radius = ksize // 2
    for row in range(0, h + radius, 1):
        y2 = h if (row + 1)> h else (row + 1)
        y1 = 0 if (row - ksize) < 0 else (row - ksize)
        for col in range(0, w + radius, 1):
            x2 = w if (col + 1)>w else (col + 1)
            x1 = 0 if (col - ksize) < 0 else (col - ksize)
            cx = 0 if (col - radius) < 0 else (col - radius)
            cy = 0 if (row - radius) < 0 else (row - radius)
            num = (x2 - x1)*(y2 - y1)
            for i in range(0, 3, 1):
                s = get_block_sum(ii, x1, y1, x2, y2, i)
                result[cy, cx][i] = s // num

    cv.imshow("integral fast blur", result)
    # cv.imwrite("./result.png", result)


src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
sum_table = cv.integral(src, sdepth=cv.CV_32S)
blur_demo(src, sum_table)

cv.waitKey(0)
cv.destroyAllWindows()
