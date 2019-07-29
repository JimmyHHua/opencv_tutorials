import cv2 as cv
import os
import numpy as np

# 把目标图放在64x128的灰色图片中间，方便计算描述子
def get_hog_descriptor(image):
    hog = cv.HOGDescriptor()
    h, w = image.shape[:2]
    rate = 64 / w
    image = cv.resize(image, (64, np.int(rate*h)))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    bg = np.zeros((128, 64), dtype=np.uint8)
    bg[:,:] = 127
    h, w = gray.shape
    dy = (128 - h) // 2
    bg[dy:h+dy,:] = gray
    fv = hog.compute(bg, winStride=(8, 8), padding=(0, 0))
    return fv

def get_data(train_data, labels, path, lableType):
    for file_name in os.listdir(path):
        img_dir = os.path.join(path, file_name)
        img = cv.imread(img_dir)
        hog_desc = get_hog_descriptor(img)
        one_fv = np.zeros([len(hog_desc)], dtype=np.float32)
        for i in range(len(hog_desc)):
            one_fv[i] = hog_desc[i][0]
        train_data.append(one_fv)
        labels.append(lableType)
    return train_data, labels

def get_dataset(pdir, ndir):
    train_data = []
    labels = []
    train_data, labels =  get_data(train_data, labels, pdir, lableType=1)
    train_data, labels =  get_data(train_data, labels, ndir, lableType=-1)

    return np.array(train_data, dtype=np.float32), np.array(labels, dtype=np.int32)


def svm_train(positive_dir, negative_dir):
    svm = cv.ml.SVM_create()
    svm.setKernel(cv.ml.SVM_LINEAR)
    svm.setType(cv.ml.SVM_C_SVC)
    svm.setC(2.67)
    svm.setGamma(5.383)
    trainData, responses = get_dataset(positive_dir, negative_dir)
    responses = np.reshape(responses, [-1, 1])
    svm.train(trainData, cv.ml.ROW_SAMPLE, responses)
    svm.save('svm_data.dat')


def elec_detect(image):
    hog_desc = get_hog_descriptor(test_img)
    print(len(hog_desc))
    one_fv = np.zeros([len(hog_desc)], dtype=np.float32)
    for i in range(len(hog_desc)):
        one_fv[i] = hog_desc[i][0]
    one_fv = np.reshape(one_fv, [-1, len(hog_desc)])
    print(len(one_fv), len(one_fv[0]))
    svm = cv.ml.SVM_load('svm_data.dat')
    result = svm.predict(one_fv)[1]
    print(result)


if __name__ == '__main__':
    #svm_train("D:/vcprojects/dataset/elec_watch/positive/", "D:/vcprojects/dataset/elec_watch/negative/")
    # cv.waitKey(0)
    test_img = cv.imread("test.jpg")
    elec_detect(test_img)
    #cv.destroyAllWindows()
