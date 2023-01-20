import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    pts1 = np.float32([[0,260],[640,260],[0,400],[640,400]])

    pts2 = np.float32([[0,0],[500,0],[0,740],[500,740]])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    result = cv2.warpPerspective(frame,matrix,(500,600))

    cv2.imshow("Frame",frame)
    cv2.imshow("Result",result)

    if cv2.waitKey(2)==27:
        break

cap.release()
cv2.destroyAllWindows()