from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

image = cv2.imread("mm.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#sobel filter
# sobel_horizontal = np.array([np.array([1,2,1]),np.array([0,0,0]),np.array([-1,-2,-1])])         #weights for horizontal edges
# sobel_vertical = np.array([np.array([-1,0,1]),np.array([-2,0,2]),np.array([-1,0,1])])           #weights for vertical edges
#
# sobel_h = ndimage.convolve(gray,sobel_horizontal)
# cv2.imshow('Sobel - Horizontal edges',sobel_h)
#
# sobel_v = ndimage.convolve(gray,sobel_vertical)
# cv2.imshow('Sobel - Vertical edges',sobel_v)
# cv2.waitKey(0)

# #prewitt filter
# prewitt_horizontal = np.array([np.array([-1,-1,-1]),np.array([0,0,0]),np.array([1,1,1])])         #weights for horizontal edges
# prewitt_vertical = np.array([np.array([-1,0,1]),np.array([-1,0,1]),np.array([-1,0,1])])           #weights for vertical edges
#
# pre_h = ndimage.convolve(gray,prewitt_horizontal)
# cv2.imshow('Prewitt - Horizontal edges',pre_h)
#
# pre_v = ndimage.convolve(gray,prewitt_vertical)
# cv2.imshow('Prewitt - Vertical edges',pre_v)
# cv2.waitKey(0)

# #robert filter
# roberts_horizontal = np.array([np.array([1,-0]),np.array([0,-1])])                   #weights for horizontal edges
# roberts_vertical = np.array([np.array([0,1]),np.array([-1,0])])                      #weights for vertical edges
#
# roberts_h = ndimage.convolve(gray,roberts_horizontal)
# cv2.imshow('Roberts - Horizontal edges',roberts_h)
#
# roberts_v = ndimage.convolve(gray,roberts_vertical)
# cv2.imshow('Roberts - Vertical edges',roberts_v)
#
# cv2.waitKey(0)

#canny edge detection
original_image = cv2.imread('mm.jpg',0)
canny = cv2.Canny(original_image,100,200)
cv2.imshow('Canny edge Detection',canny)
cv2.waitKey(0)