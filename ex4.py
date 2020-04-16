import cv2
import numpy as np
import copy
import scipy.io as sio


mdict = sio.loadmat("./hw2_data/bilateral.mat")
image = mdict["img_noisy"]
cv2.imshow("noisy image", image)

bilateral = cv2.bilateralFilter(image, 7, 1.5, 1.5)
cv2.imshow("bilateral image", bilateral)

cv2.waitKey()
cv2.destroyAllWindows()


