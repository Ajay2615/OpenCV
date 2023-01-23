# Pyramid using OpenCV


Image Pyramids are one of the most beautiful concept of image processing.Normally, we work with images with default resolution but many times we need to change the resolution (lower it) or resize the original image in that case image pyramids comes handy. The pyrUp() function increases the size to double of its original size and pyrDown() function decreases the size to half. If we keep the original image as a base image and go on applying pyrDown function on it and keep the images in a vertical stack, it will look like a pyramid. The same is true for upscaling the original image by pyrUp function.


![Pyramid](https://user-images.githubusercontent.com/99254412/214066578-41b44d7f-2516-42ac-8932-dd6e79bddc67.png)
