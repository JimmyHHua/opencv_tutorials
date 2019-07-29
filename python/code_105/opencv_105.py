import cv2 as cv
import numpy as np


if __name__ == '__main__':
    image = cv.imread("src.jpg")
    # 原图太大，降低原图分辨率
    #test_img = cv.resize(image, (0, 0), fx=0.2, fy=0.2)
    cv.imshow("input", test_img)
    gray = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)
    print(gray.shape)
    h, w = test_img.shape[:2]
    # 加载训练好的模型
    svm = cv.ml.SVM_load('svm_data.dat')
    # 为了筛选框，记录框坐标总和以及框的个数，为了最后求出所有候选框的均值框
    sum_x = 0
    sum_y = 0
    count = 0
    hog = cv.HOGDescriptor()
    # 为了加快计算，窗口滑动的步长为4，一个cell是8个像素
    for row in range(64, h-64, 4):
        for col in range(32, w-32, 4):
            win_roi = gray[row-64:row+64,col-32:col+32]
            hog_desc = hog.compute(win_roi, winStride=(8, 8), padding=(0, 0))
            one_fv = np.zeros([len(hog_desc)], dtype=np.float32)
            for i in range(len(hog_desc)):
                one_fv[i] = hog_desc[i][0]
            one_fv = one_fv.reshape(-1, len(hog_desc))
            result = svm.predict(one_fv)[1]
            # 统计正样本
            if result[0][0] > 0:
                sum_x += (col-32)
                sum_y += (row-64)
                count += 1
                cv.rectangle(test_img, (col-32, row-64), (col+32, row+64), (0, 233, 255), 1, 8, 0)

    # 求取均值框
    x = sum_x // count
    y = sum_y // count
    cv.rectangle(test_img, (x, y), (x+64, y+128), (0, 0, 255), 2, 8, 0)
    cv.imshow("result", test_img)
    cv.imwrite('result.jpg', test_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
