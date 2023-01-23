import numpy as np
import cv2
cap =cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gaussian = cv2.bilateralFilter(frame,9,50,50)

    hsv = cv2.cvtColor(gaussian,cv2.COLOR_BGR2HSV)
    lower_values = np.array([0,120,151])
    upper_value = np.array([33,255,255])

    mask = cv2.inRange(hsv,lower_values,upper_value)

    countours ,_= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[-2:]
    for countour in countours:
        cv2.drawContours(frame,countour,-1,(0,0,255),3)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(2)==27:
        break

cv2.destroyAllWindows()












