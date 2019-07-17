import cv2 as cv

#capture = cv.VideoCapture(1)
detector = cv.CascadeClassifier("lbpcascade_frontalface_improved.xml")
image = cv.imread('people.jpg')

faces = detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=1,
                                  minSize=(30, 30), maxSize=(200, 200))
for x, y, width, height in faces:
    cv.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv.LINE_8, 0)

cv.imshow("faces", image)
cv.imwrite("faces_lbp.jpg", image)

c = cv.waitKey(0)
'''
while True:
    ret, image = capture.read()
    if ret is True:
        cv.imshow("frame", image)
        faces = detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=1,
                                          minSize=(30, 30), maxSize=(120, 120))
        for x, y, width, height in faces:
            cv.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv.LINE_8, 0)
        cv.imshow("faces", image)
        c = cv.waitKey(50)
        if c == 27:
            break
    else:
        break
'''
cv.destroyAllWindows()

