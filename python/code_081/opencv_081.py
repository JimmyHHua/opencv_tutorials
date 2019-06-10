import numpy as np
import cv2 as cv


def harris(image, opt=1):
    # Detector parameters
    blockSize = 2
    apertureSize = 3
    k = 0.04
    # Detecting corners
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    # Normalizing
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    
    # Drawing a circle around corners
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)
    # output
    return image


src = cv.imread("chessboard.jpg")
cv.imshow("input", src)
result = harris(src)
cv.imshow('result', result)
cv.imwrite('result.jpg', result)
cv.waitKey(0)
cv.destroyAllWindows()
"""
# For video:
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv.imwrite("input.png", frame)
    cv.imshow('input', frame)
    result = harris(frame)
    cv.imshow('result', result)
    k = cv.waitKey(5)&0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
"""