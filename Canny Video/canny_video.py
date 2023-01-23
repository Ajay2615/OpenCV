import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    ret,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    lower_val = np.array([102,123,3])
    upper_val = np.array([142,255,245])

    mask = cv2.inRange(hsv,lower_val,upper_val)

    res = cv2.bitwise_and(frame,frame,mask=mask)
    canny = cv2.Canny(frame,100,200)
    cv2.imshow("Canny",canny)

    if cv2.waitKey(2)==27:
        break

cv2.destroyAllWindows()