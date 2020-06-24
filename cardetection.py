#AS2016467
#W.B.M.Perera

import os
import re
import cv2 # opencv library
import numpy as np
import matplotlib.pyplot as plt
 
# Create a VideoCapture object and read from input file

cap = cv2.VideoCapture('cardetection.mp4')
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml') 

old_frame=None
diff_frame=None

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")
 
# Read until video is completed
while (cap.isOpened()):
    # step 1----> read the video frame by frame
    ret, frames = cap.read()
    if ret == True:

        # step 2----> gray conversion
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray',gray)

        # step 3----> apply frames difference
        

        
        
        if old_frame is not None:
          
          diff_frame=cv2.absdiff(gray,old_frame)
          cv2.imshow('frame_differencing',diff_frame)
          
          # step 4----> apply image thresholding to the gray frames
          ret, thresh = cv2.threshold(diff_frame,50, 255, cv2.THRESH_BINARY)
          cv2.imshow('threshold',thresh)

          # step 5----> apply image dilation to the frames which is threshold before
          kernel = np.ones((2,2),np.uint8)
          dilated = cv2.dilate(thresh,kernel,iterations = 1)
          cv2.imshow('Dilated',dilated)

          #step 5-----> apply car cacade classifier to dilated frames and bound the cars                            
          cars = car_cascade.detectMultiScale(dilated,1.1,3)


          
          for (x,y,w,h) in cars:
        
            cv2.rectangle(frames,(x,y),(x +w, y +h) ,(0 ,0,255),2)
            cv2.rectangle(frames, (x, y - 40), (x + w, y), (0,0,255))
            cv2.putText(frames, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
            cv2.imshow('car Detection system',frames)


                                      
      
        old_frame=gray


## 
        # Press Q on keyboard to  exit
        if cv2.waitKey(20)== ord('q'):
            break
  
    # Break the loop
    else:
        break
## 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
