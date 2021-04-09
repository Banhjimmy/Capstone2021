# Program runs with Python2

import cv2
import imutils
import time

# Uncomment These next Two Line for Pi Camera
# camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cap = cv2.VideoCapture(camSet)

# Uncomment next line if usb camera in use 
# cap = cv2.VideoCapture(0)

ret, HDframe = cap.read()

def takePicture():
    (grabbed, HDframe) = cap.read()
    cv2.waitKey(1)
    image = '/home/spring2021/Desktop/EE/HDimages/HDframe.jpg' 
    cv2.imwrite(image, HDframe)
    cap.release()
    return image

takePicture()
