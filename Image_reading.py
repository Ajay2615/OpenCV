import cv2

image = cv2.imread('wallpaper2you_351440.jpg')

img_gray = cv2.imread('wallpaper2you_351440.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow("MyImage",image)

cv2.imshow("IMG_GRAYSCALE",img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()