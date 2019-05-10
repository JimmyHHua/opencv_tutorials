import cv2 as cv
import cv2 as cv
import numpy as np


def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=np.int)
    cols = np.random.randint(0, w, nums, dtype=np.int)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image


def gaussian_noise(image):
    noise = np.zeros(image.shape, image.dtype)
    m = (15, 15, 15)
    s = (30, 30, 30)
    cv.randn(noise, m, s)
    dst = cv.add(image, noise)
    cv.imshow("gaussian noise", dst)
    return dst


src = cv.imread("./test.png")
cv.imshow("input", src)
h, w = src.shape[:2]
src = gaussian_noise(src)

result1 = cv.blur(src, (5, 5))
cv.imshow("result-1", result1)

result2 = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("result-2", result2)

result3 = cv.medianBlur(src, 5)
cv.imshow("result-3", result3)

result4 = cv.fastNlMeansDenoisingColored(src, None, 15, 15, 10, 30)
cv.imshow("result-4", result4)

cv.waitKey(0)
cv.destroyAllWindows()






