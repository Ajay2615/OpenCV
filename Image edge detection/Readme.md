# Image edge detection using OpenCV

Original Image: 
![og image](https://user-images.githubusercontent.com/99254412/214059326-dcb4cf25-2850-4aa3-8266-a4d4c4197b72.png)

Laplacian Image: Laplacian Operator is also a derivative operator which is used to find edges in an image. It is a second order derivative mask. In this mask we have two further classifications one is Positive Laplacian Operator and other is Negative Laplacian Operator.
![Laplacian image](https://user-images.githubusercontent.com/99254412/214059445-5bcc8a11-c5ee-4c79-b7f3-dcc63550ac0e.png)

Horizontal Sobel derivative (Sobel x): It is obtained through the convolution of the image with a matrix called kernel which has always odd size. The kernel with size 3 is the simplest case.
![SobelX](https://user-images.githubusercontent.com/99254412/214059662-b08e4d08-f23b-4a96-a436-80b9bea6c336.png)

Vertical Sobel derivative (Sobel y): It is obtained through the convolution of the image with a matrix called kernel which has always odd size. The kernel with size 3 is the simplest case.
![SobelY](https://user-images.githubusercontent.com/99254412/214059730-fd8e578e-498e-45a3-ba24-2e053d7a2002.png)

Convolution is calculated by the following method: Image represents the original image matrix and filter is the kernel matrix.
![Com_sobel](https://user-images.githubusercontent.com/99254412/214059918-0331e52c-4cc0-44e2-9a0b-318caa5b2f2c.png)
