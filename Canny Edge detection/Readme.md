# Canny edge detection of an image using OpenCV

Original image converted to Black & White:

![og image ](https://user-images.githubusercontent.com/99254412/214061521-4a46d869-fa5c-4968-8a0d-9deed4415caf.png)


Sobel X image:

![sobelx](https://user-images.githubusercontent.com/99254412/214061650-af31d050-8040-45c7-a7f8-756bf43b02bf.png)

Sobel Y image:

![sobely](https://user-images.githubusercontent.com/99254412/214061670-673bc304-4c59-4951-a3fb-314351aba50e.png)

Com image:

![com](https://user-images.githubusercontent.com/99254412/214061800-0f74a877-2a7c-49ed-8390-47e409457833.png)


Canny Edge detection is an Algorithm consisting of 4 major steps:
Reduce Noise using Gaussian Smoothing.
Compute image gradient using Sobel filter.
Apply Non-Max Suppression or NMS to just jeep the local maxima
Finally, apply Hysteresis thresholding which that 2 threshold values T_upper and T_lower which is used in the Canny() function.


Canny Edge image: 

![canny](https://user-images.githubusercontent.com/99254412/214061889-3b7da527-2d0b-41bd-927a-be93ee6fb499.png)
