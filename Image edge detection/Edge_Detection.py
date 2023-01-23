import cv2
# from cv2 import Laplacian
import numpy as np

img = cv2.imread('batman_vs_superman.jpg')

img = cv2.resize(img,(600,400))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(img_gray,cv2.CV_64F,ksize=3)
laplacian = np.uint8(np.absolute(laplacian))

sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize=3)

sobelX = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobely))

com_sobel = cv2.bitwise_or(sobelX,sobely)

cv2.imshow("Actual",img)
cv2.imshow("laplacian",laplacian)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobely",sobely)
cv2.imshow("com_sobel",com_sobel)


cv2.waitKey(0)
cv2.destroyAllWindows()