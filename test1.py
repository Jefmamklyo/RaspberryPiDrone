import cv2 as cv
import numpy as np
import time

cam = cv.VideoCapture(1, cv.CAP_V4L2)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
currentFrame = 0
prevFrame = 0



if __name__ == "__main__":
    print(__name__)
while True:
    ret, frame = cam.read()

    if not ret:
        print("TRhis is breaking")
        break

    currentFrame = time.time()
    fps= 1/ (currentFrame - prevFrame)
    prevFrame = currentFrame
    cv.putText(img = frame, text = f"fps:{int(fps)}", org=(7,70), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 3, color = (100, 255, 100), thickness = 2, lineType = cv.LINE_AA)

    cv.imshow("frame", frame)


    exitKey= cv.waitKey(1)
    idle = "F"
    if exitKey == ord('l'):
        break
        
#exit sequence
cam.release() #automatically releases the cameras
cv.destroyAllWindows()