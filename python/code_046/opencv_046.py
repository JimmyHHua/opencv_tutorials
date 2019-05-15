import cv2 as cv
import numpy as np


def connected_components_demo(src):
    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    cv.imwrite('binary.png', binary)

    output = cv.connectedComponents(binary, connectivity=8, ltype=cv.CV_32S)
    num_labels = output[0]
    print(num_labels)  # output: 5
    labels = output[1]

    # 构造颜色
    colors = []
    for i in range(num_labels):
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))
    colors[0] = (0, 0, 0)

    # 画出连通图
    h, w = gray.shape
    image = np.zeros((h, w, 3), dtype=np.uint8)
    for row in range(h):
        for col in range(w):
            image[row, col] = colors[labels[row, col]]

    cv.imshow("colored labels", image)
    cv.imwrite("labels.png", image)
    print("total componets : ", num_labels - 1)



src = cv.imread("pill.png")
h, w = src.shape[:2]
connected_components_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()