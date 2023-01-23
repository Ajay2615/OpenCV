# from tokenize import PlainToken
# from winsound import PlaySound
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("download (1).jfif",0)

histogram_01 = cv2.calcHist([img],[0],None,[256],[0,256])

#img - original image or input image
#[0] - channels  
#None - full image
#[256] - bins
#[0,256] - range

plt.plot(histogram_01)
plt.show()


