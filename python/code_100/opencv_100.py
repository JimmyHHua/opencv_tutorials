import cv2 as cv

if __name__ == '__main__':
    src = cv.imread("pedestrian.png")
    cv.imshow("input", src)
    hog = cv.HOGDescriptor()
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
    # Detect people in the image
    (rects, weights) = hog.detectMultiScale(src,
                                            winStride=(4, 4),
                                            padding=(8, 8),
                                            scale=1.25,
                                            useMeanshiftGrouping=False)
    for (x, y, w, h) in rects:
        cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("hog-detector", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
