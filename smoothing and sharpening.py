import cv2

#smoothing
image = cv2.imread("lenna.jpg")
cv2.imshow("Original", image)

#normalized blur
blurred = cv2.blur(image, (9,9))
cv2.imshow("blurred image", blurred)
cv2.waitKey(0)

#median blur
# blurred = cv2.medianBlur(image, 9)
# cv2.imshow("blurred image", blurred)
# cv2.waitKey(0)

# #sharpening
# image = cv2.imread("mm.jpg")
# cv2.imshow("Original", image)
# new_image = cv2.Laplacian(image,cv2.CV_64F)
# cv2.imshow("Image", new_image)
# cv2.waitKey(0)