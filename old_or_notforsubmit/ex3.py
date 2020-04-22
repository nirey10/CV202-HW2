import cv2
import numpy as np
import copy
import scipy.io as sio


mdict = sio.loadmat("./hw2_data/are_these_separable_filters.mat")
# print([k for k in mdict.keys() if not k.startswith("__")])
K1 = mdict["K1"]
K2 = mdict["K2"]
K3 = mdict["K3"]

def zeroSmallNumbers(arr):
    newarr = []
    count = 0
    for item in arr:
        if np.abs(item) < 0.000000000001:
            newarr.append(0)
        else:
            newarr.append(item)
            count += 1
    return newarr, count


U1, s1, V1 = np.linalg.svd(K1, full_matrices=True)
U2, s2, V2 = np.linalg.svd(K2, full_matrices=True)
U3, s3, V3 = np.linalg.svd(K3, full_matrices=True)

singular1, count1 = zeroSmallNumbers(s1)
singular2, count2 = zeroSmallNumbers(s2)
singular3, count3 = zeroSmallNumbers(s3)

print("Singular Values for K1: \n" + str(np.diag(singular1)))
print("Kernel is separable\n" if count1 == 1 else "Kernel is not separable\n")
print("Singular Values for K2: " + str(np.diag(singular2)))
print("Kernel is separable\n" if count2 == 1 else "Kernel is not separable\n")
print("Singular Values for K3: " + str(np.diag(singular3)))
print("Kernel is separable\n" if count3 == 1 else "Kernel is not separable\n")


