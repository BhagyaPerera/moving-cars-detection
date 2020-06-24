# moving-cars-detection
This project describes the use of image processing to detect the moving cars in video that was taken by stationary camera using image processing with python-OpenCV. As human beings we can identify the moving objects very fast. However, computers have to perform some algorithms to extract features of objects in order to identify the objects. 
Following steps were performed to set up the car detection and tracking pipeline for a video-feed obtained from the camera.



1. Video capture and frames extracting
Video is a group of frames stacked together in sequence. Therefore, when we see an object moving in
the video, it means that the object is located in a different position in each successive frame. If we
assume that no other object moves in a pair of consecutive frames except that object, then the pixel
difference between the first frame and the second frame will highlight the pixels of the moving object.
Now, we will get the pixels and coordinates of the moving object. For this implementation video is
reading from a file frame by frame.

2. Gray Scale Conversion
Generally, the grayscale intensity is stored as an 8-bit integer, giving 256 possible different shades of
grayscale from black to white. If these levels are evenly spaced, the difference between successive gray
levels will be significantly better than the gray level resolution of the human eye. Gray scale images are
just images in which the only color is shaded gray. The reason for distinguishing such an image from any
other kind of a color image is that less information needs to be provided for each pixel. Therefore, in this
implementation original video is converted to grayscale.

3. frame differencing
To find the moving cars initially I get the difference of pixel values in each consecutive gray scale frame
by assuming all the other objects are not moving.


4. Image Threshold
The fourth step is Image thresholding. In this method, the pixel values of a grayscale image are
assigned one of the two values representing black and white colors based on a threshold. So, if
the value of a pixel is greater than a threshold value, it is assigned one value, else it is assigned
the other value. For this implementation threshold value is taken as 100.Threshold gives clear
images with background removal for more extent.


5. Image Dilation
This is a convolution operation on the image, where the kernel (matrix) passes over the entire
image. Here 3x3 matrix is taken as a kernel. Kernel is taken over the entire image which the
threshold is applied. Dilation is a morphological operation. Since dilation adds pixels to the
boundaries of an object, we can clearly see the object boundaries in the dilation step.



6. Car detection and bound the object
Pre-trained car detection cascade classifier is applied to the dilated image. In this stage, all the
moving cars are detected and display it with a rectangle which is bounded the car. cascade
classifier is saved in the file as “haarcascade_car.xml”.
