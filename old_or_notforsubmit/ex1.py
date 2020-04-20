import cv2
import numpy as np
import copy

image = cv2.imread("./hw2_data/mandrill.png")
gaussian7 = image.copy()
gaussian21 = image.copy()
uniform = image.copy()

cv2.imshow("Original", image)

gaussian7 = cv2.GaussianBlur(gaussian7,(7,7),3)
cv2.imshow("gaussian 7x7", gaussian7)

gaussian21 = cv2.GaussianBlur(gaussian21,(21,21),10)
cv2.imshow("gaussian 21x21", gaussian21)

# h = np.ones((21, 21)) / (21 ** 2)
uniform = cv2.blur(uniform, (21, 21))
cv2.imshow("uniform blur", gaussian21)

cv2.waitKey()
cv2.destroyAllWindows()