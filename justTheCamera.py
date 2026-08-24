import cv2 as cv
import numpy as np
import time



def waterShed(frame):
    #pre procxessing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)

    kernal = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))

    _, thresh = cv.threshold(blur, 0,255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU) #binareise iamge

    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernal, iterations =2)

    #backroudn and forgroudn (bg, fg)
    sureBg =  cv.dilate(opening, kernal, iterations = 2)
    distTransform = cv.distanceTransform(opening, cv.DIST_L2,5)
    _, sureFg = cv.threshold(distTransform, 0.4*distTransform.max(),255,0)
    sureFg = np.uint8(sureFg)

    unknown = cv.subtract(sureFg, sureBg)

    #lkabeling markers
    _, markers = cv.connectedComponents(sureFg)
    markers = markers +1
    markers[unknown = 255] = 0
    markers = cv.watershed(frame.copy(), markers)


    return sureBg

cam = cv.VideoCapture(0, cv.CAP_V4L2)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 320)
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

    processedFrame = waterShed(frame)
    currentFrame = time.time()
    fps= 1/ (currentFrame - prevFrame)
    prevFrame = currentFrame

    cv.putText(img = processedFrame, text = f"fps:{int(fps)}", org=(7,70), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 3, color = (100, 255, 100), thickness = 2, lineType = cv.LINE_AA)

    cv.imshow("frame", processedFrame)

    exitKey= cv.waitKey(1)
    idle = "F"
    if exitKey == ord('l'):
        break
        
#exit sequence
cam.release() #automatically releases the cameras
cv.destroyAllWindows()