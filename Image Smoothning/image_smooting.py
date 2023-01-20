import cv2
import numpy as np

img = cv2.imread('threshold.jpg')

kernel = np.ones((5,5),np.float32)/25

h_filter = cv2.filter2D(img,-1,kernel)#-1 is just a depth over here

blur = cv2.blur(img,(8,8))

gaussain = cv2.GaussianBlur(img,(5,5),0)

med = cv2.medianBlur(img,5)

bi = cv2.bilateralFilter(img,9,50,50)
bi_70 = cv2.bilateralFilter(img,9,20,20)

cv2.imshow("Actual image",img)
cv2.imshow("h_filter",h_filter)
cv2.imshow("Blur",blur)
cv2.imshow("gaussain",gaussain)
cv2.imshow("med",med)
cv2.imshow("bi",bi)
cv2.imshow("bi_70",bi_70)

cv2.waitKey(0)
cv2.destroyAllWindows()