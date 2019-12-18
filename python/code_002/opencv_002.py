import cv2

src = cv2.imread("./test.png")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png', gray)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

