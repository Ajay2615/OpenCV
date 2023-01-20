import cv2
import numpy as np

img = cv2.imread('download.jfif')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# print(img_gray.shape)
rows,cols = img_gray.shape
# M = np.float32([[1,0,300],[0,1,300]])

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

dst = cv2.warpAffine(img_gray,M,(cols,rows))

cv2.imshow("Original Image",img)
cv2.imshow("Affine Image",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

