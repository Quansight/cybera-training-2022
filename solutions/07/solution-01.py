## Solution for Notebook 06 - Exercise 01

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

I = np.ones((16,16), dtype='float')
I[:8,:8] = np.zeros((8,8))
plt.imshow(I, cmap='gray')
plt.plot(7,7,'ro')

Ix = cv.Sobel(I, cv.CV_64F, 1, 0, ksize=5)
Iy = cv.Sobel(I, cv.CV_64F, 0, 1, ksize=5)

Ix2 = np.multiply(Ix,Ix)
Iy2 = np.multiply(Iy,Iy)
IxIy = np.multiply(Ix,Iy)

SIx2 = cv.blur(Ix2, (5,5)).flatten()
SIy2 = cv.blur(Iy2, (5,5)).flatten()
SIxIy = cv.blur(IxIy, (5,5)).flatten()

M = np.vstack((SIx2, SIxIy, SIxIy, SIy2 )).reshape(4,16,16)
print('M at (7,7) =\n', M[:,7,7].reshape(2,2))