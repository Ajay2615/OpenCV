import cv2
from matplotlib.colors import from_levels_and_colors
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H","Trackbars",0,179,nothing)
cv2.createTrackbar("L - S","Trackbars",0,255,nothing)
cv2.createTrackbar("L - V","Trackbars",0,255,nothing)
cv2.createTrackbar("U - H","Trackbars",179,179,nothing)
cv2.createTrackbar("U - S","Trackbars",0,255,nothing)
cv2.createTrackbar("U - V","Trackbars",0,255,nothing)

while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H","Trackbars")
    print('l_h',l_h)
    l_s = cv2.getTrackbarPos("L - S","Trackbars")
    print('l_s',l_s)
    l_v = cv2.getTrackbarPos("L - V","Trackbars")
    print('l_v',l_v)
    u_h = cv2.getTrackbarPos("U - H","Trackbars")
    print('u_h',u_h)
    u_s = cv2.getTrackbarPos("U - S","Trackbars")
    print('u_s',u_s)
    u_v = cv2.getTrackbarPos("U - V","Trackbars")
    print('u_v',u_v)


    # lower_value = np.array([l_h,l_s,l_v])
    # upper_value = np.array([u_h,u_s,u_v])
    # l_h 102
    # l_s 123
    # l_v 3
    # u_h 142
    # u_s 255
    # u_v 245
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    lower_val = np.array([102,123,3])
    upper_val = np.array([142,255,245])

    mask = cv2.inRange(hsv,lower_val,upper_val)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Original Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("result",result)
    if(cv2.waitKey(2)==27):
        break

cap.release()
cv2.destroyAllWindows()
