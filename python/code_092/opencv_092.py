import cv2 as cv

capture = cv.VideoCapture(1)
face_detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
eye_detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
smile_detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_smile.xml")

image = cv.imread('people.jpg')
faces = face_detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=3,
                                  minSize=(50, 50), maxSize=(300, 300))
for x, y, width, height in faces:
    cv.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv.LINE_8, 0)
    roi = image[y:y+height,x:x+width]

    eyes = eye_detector.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=5,
                                       minSize=(20, 20), maxSize=(30,30))
    smiles = smile_detector.detectMultiScale(roi, scaleFactor=1.05, minNeighbors=2,
                                             minSize=(20, 20))

    for ex, ey, ew, eh in eyes:
        cv.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    for sx, sy, sw, sh in smiles:
        cv.rectangle(roi, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
        cv.putText(image, 'Smile', (x+10, y-7), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv.imshow("faces", image)
cv.imwrite("face_smile_eye.jpg", image)
cv.waitKey(0)
'''
while True:
    ret, image = capture.read()
    if ret is True:
        cv.imshow("frame", image)
        faces = face_detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=3,
                                          minSize=(30, 30), maxSize=(300, 300))
        for x, y, width, height in faces:
            cv.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv.LINE_8, 0)
        roi = image[y:y+height,x:x+width]
        smiles = smile_detector.detectMultiScale(roi, scaleFactor=1.7, minNeighbors=3,
                                               minSize=(15, 15), maxSize=(100, 100))
        for sx, sy, sw, sh in smiles:
            cv.rectangle(roi, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)

        cv.imshow("faces", image)
        c = cv.waitKey(50)
        if c == 27:
            break
    else:
        break
'''
cv.destroyAllWindows()

