# l_h 0
# l_s 52
# l_v 0
# u_h 35
# u_s 163
# u_v 170
import cv2
import numpy as np

gray = cv2.imread("coin.jfif",0)

output = gray
#img = cv2.imread("water_coins.jpg",cv2.COLOR_BHR2GRAY)

gray = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=50)

detected_circles = np.uint16(np.around(circles))
print("Shape",  detected_circles.shape)

for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),1)

cv2.imshow("ORiginal",gray)
cv2.imshow("Result",output)
cv2.waitKey(0)
cv2.destroyAllWindows()

