import cv2
import matplotlib.pyplot as plt

img = cv2.imread('batman_vs_superman.jpg')

# img = cv2.resize(img,(200,200))
# img=cv2.imread("cropped_shield.jpg")
# img1=cv2.pyrUp(img)
# img2=cv2.pyrUp(img1)
# img3=cv2.pyrUp(img2)
img1=cv2.pyrDown(img)
img2=cv2.pyrDown(img1)
img3=cv2.pyrDown(img2)


cv2.imshow("original_image",img)
cv2.imshow('pyrUP1',img1)
cv2.imshow('pyrUP2',img2)
cv2.imshow('pyrUP3',img3)

cv2.waitKey(0)

cv2.destroyAllWindows()

# for i in range(4):
#     plt.subplot(2,2,i+1)

#     layers = cv2.pyrDown(img[i])

#     plt.imshow(layers)
#     cv2.imshow("str(i)",layers)
#     cv2.waitKey(0)

# cv2.destroyAllWindows()