import cv2 as cv
import numpy as np

cam1  = cv.VideoCapture("/dev/video0", cv.CAP_V4L2)
cam2 = cv.VideoCapture("/dev/video2", cv.CAP_V4L2)


#srtyting resultion
cam1.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cam1.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
cam1.set(cv.CAP_PROP_FPS, 15)

cam2.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cam2.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
cam2.set(cv.CAP_PROP_FPS, 15)


checkerBoardSize = (9,6)
checkerSquareSize = 0.025 #meters

baseLine = 8 #distance between cameras cm
focalLenght = 3015 #camera fiocal lenght foudn from tuning




print("Camera 1:",cam1.isOpened())
print("Casmera 2:", cam2.isOpened())


while True:
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()


        if ret1:
            cv.imshow("frame", frame1)
        if ret2:
            cv.imshow("frame2", frame2)


        exitKey= cv.waitKey(1)
        idle = "F"
        if exitKey == ord('l'):
            break
cam1.release()
cam2.release()
            