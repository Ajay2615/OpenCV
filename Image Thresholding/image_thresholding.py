import cv2
import numpy as np

img = cv2.imread('download.jfif',0)

_ , th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_ , th2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_ , th3 = cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_ , th4 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_ , th5 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("original image",img)
cv2.imshow("Binary",th1)
cv2.imshow("THRESH_BINARY_INV",th2)
cv2.imshow("THRESH_TRUNC",th3)
cv2.imshow("THRESH_TOZERO",th4)
cv2.imshow("THRESH_TOZERO_INV",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()

