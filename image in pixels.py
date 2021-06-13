import cv2
image = cv2.imread("lenna.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray)
cv2.imshow("Image", image)
cv2.waitKey(0)

# from PIL import Image
# import numpy as np
#
# w, h = 512, 512
# data = np.zeros((h, w, 3), dtype=np.uint8)
# data[0:256, 0:256] = [125, 125, 125] # grey patch in upper left
# img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()