#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date:   2020-02-24 18:06:06

@author: JimmyHua
"""

import cv2
import numpy as np

# load the qrcode
src = cv2.imread("qrcode.png")
cv2.imshow("image", src)
# gray image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# set qrcoder
qrcoder = cv2.QRCodeDetector()
codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)
print(points)
result = np.copy(src)
cv2.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)
print("qrcode information is :\n%s"% codeinfo)
cv2.imshow("result", result)
cv2.imwrite("result.png", result)
code_roi = np.uint8(straight_qrcode)
cv2.imshow("qrcode roi", code_roi)
cv2.imwrite("qrcode_roi.png", code_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()