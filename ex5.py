import cv2
import numpy as np
import copy
import scipy.io as sio

image = cv2.imread("./hw2_data/ascent.jpg", 0)
cv2.imshow("Original", image)

hx1, hy0 = cv2.getDerivKernels(1,0,5)
hx0, hy1 = cv2.getDerivKernels(0,1,5)
x_filter = np.ones(shape=(5,5))
x_filter = x_filter*hx1
y_filter = np.ones(shape=(5,5))
hy1 = hy1.transpose()
y_filter = hy1*y_filter

def getDirectionalFilteredImage(image, theta):
    u = np.sin(theta)
    v = np.cos(theta)
    filter = u*x_filter + v*y_filter
    filteredImage = cv2.filter2D(image, -1, filter)
    return filteredImage, filter

angles = [0, 45, 60, 75, 90]
for angle in angles:
    filteredImage, filter = getDirectionalFilteredImage(image, angle)
    print("the " + str(angle) + " angle filter is: \n" + str(filter))
    cv2.imshow("angle " + str(angle) + "", filteredImage)

cv2.waitKey()
cv2.destroyAllWindows()


