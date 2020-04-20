import cv2
import numpy as np
import copy
import scipy.io as sio

image = cv2.imread("./hw2_data/ascent.jpg", 0)
cv2.imshow("Original", image)

def getDirectionalFilteredImage(image, theta):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    u = np.sin(theta)
    v = np.cos(theta)
    return u*sobel_x + v*sobel_y

cv2.imshow("sobel_0", getDirectionalFilteredImage(image, 0))
cv2.imshow("sobel_45", getDirectionalFilteredImage(image, 45))
cv2.imshow("sobel_60", getDirectionalFilteredImage(image, 60))
cv2.imshow("sobel_75", getDirectionalFilteredImage(image, 75))
cv2.imshow("sobel_90", getDirectionalFilteredImage(image, 90))

cv2.waitKey()
cv2.destroyAllWindows()


