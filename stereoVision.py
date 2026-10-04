import cv2 as cv
import numpy as np

cam1  = cv.VideoCapture(0, cv.CAP_V4L2)
cam2 = cv.VideoCapture(1, cv.CAP_V4L2)

while True:
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()


        cv.imshow("frame", frame1)
        cv.imshow("frame", frame12


        exitKey= cv.waitKey(1)
        idle = "F"
        if exitKey == ord('l'):
            break
            