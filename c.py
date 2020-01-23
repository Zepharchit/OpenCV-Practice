import cv2
import numpy as np
import matplotlib.pyplot as pyplot

img =  cv2.imread('./abx.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)