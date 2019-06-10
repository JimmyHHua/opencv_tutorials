import numpy as np
import cv2


def process(image, opt=1):
    # Detecting corners
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 35, 0.05, 10)
    print(len(corners))
    for pt in corners:
        print(pt)
        b = np.random.random_integers(0, 256)
        g = np.random.random_integers(0, 256)
        r = np.random.random_integers(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv2.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
    # output
    return image


src = cv2.imread("blox.jpg")
cv2.imshow("input", src)
result = process(src)
cv2.imshow('result', result)
cv2.imwrite('result.jpg',result)
cv2.waitKey(0)
cv2.destroyAllWindows()