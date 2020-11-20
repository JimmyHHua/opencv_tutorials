import numpy as np
import cv2 as cv

W_in = 224
H_in = 224
modelTxt = "../model/color/colorization_deploy_v2.prototxt";
modelBin = "../model/color/colorization_release_v2.caffemodel";
pts_txt = "../model/color/pts_in_hull.npy";

# Select desired model
net = cv.dnn.readNetFromCaffe(modelTxt, modelBin)
pts_in_hull = np.load(pts_txt) # load cluster centers

# populate cluster centers as 1x1 convolution kernel
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull.astype(np.float32)]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]

frame = cv.imread("4.jpg")
h, w = frame.shape[:2]
img_rgb = (frame[:,:,[2, 1, 0]] * 1.0 / 255).astype(np.float32)

img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
img_l = img_lab[:,:,0] # pull out L channel
(H_orig,W_orig) = img_rgb.shape[:2] # original image size

# resize image to network input size
img_rs = cv.resize(img_rgb, (W_in, H_in))
img_lab_rs = cv.cvtColor(img_rs, cv.COLOR_RGB2Lab)
img_l_rs = img_lab_rs[:,:,0]
img_l_rs -= 50 # subtract 50 for mean-centering

# run network
net.setInput(cv.dnn.blobFromImage(img_l_rs))
ab_dec = net.forward()[0,:,:,:].transpose((1,2,0))

(H_out,W_out) = ab_dec.shape[:2]
ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))
img_lab_out = np.concatenate((img_l[:,:,np.newaxis],ab_dec_us),axis=2)

img_bgr_out = np.clip(cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR), 0, 1)
print(img_bgr_out.shape)
frame = cv.resize(frame, (w, h))
cv.imshow('origin', frame)
gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)
#cv.imwrite('gray.jpg', gray)
# fix 4.0 imshow issue
cv.normalize(img_bgr_out, img_bgr_out, 0, 255, cv.NORM_MINMAX)
cv.imshow('colorized', cv.resize(np.uint8(img_bgr_out), (w, h)))
cv.imwrite('4color.jpg', cv.resize(np.uint8(img_bgr_out), (w, h)))
cv.waitKey(0)
cv.destroyAllWindows()
