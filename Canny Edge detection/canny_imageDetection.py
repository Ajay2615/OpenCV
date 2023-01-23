import cv2 
import numpy as np

image = cv2.imread('batman_vs_superman.jpg',0)
image = cv2.resize(image,(600,400))

sobelX = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
sobelX = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobely))
com_sobel = cv2.bitwise_or(sobelX,sobely)

canny_ot = cv2.Canny(image,80,150)

cv2.imshow("original",image)
cv2.imshow("sobelx",sobelX)
cv2.imshow("sobely",sobely)
cv2.imshow("com",com_sobel)
cv2.imshow("Canny",canny_ot)

cv2.waitKey(0)
cv2.destroyAllWindows()