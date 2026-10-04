import cv2 as cv
import numpy as np
import time
import tracemalloc




def orbBenchMark(img, **kwarg):
    orb =cv.ORB_create(nfeatures = 500, **kwarg)
    start = time.perf_counter()
    tracemalloc.start() #start memory tracing
    keypoints, descriptor = orb.detectAndCompute(img, None)
    currentMemory, peakMemory = tracemalloc.get_traced_memory() #get peak memoery usage
    tracemalloc.stop()
    elapsed = (time.perf_counter() - start) * 1000 #convert form millis to secs
    keypointsImage = cv.drawKeypoints(img, keypoints, None, color = (0,255,0), flags = 0) #drawing keypoijnt but not size asnd orientation 
    print(f"KeypointCount = {len(keypoints)} || elasped time = {elapsed}, peakMemoryUasge = {peakMemory}")

    return len(keypoints), elapsed, peakMemory, keypointsImage









#grab image from 1 frame |||||| TEMPORARY WIFI {PROBLEMS CAN'T DOWNLAOD IAMGES PLEASE MAKE THIS AN IAMGEW} ||

cam = cv.VideoCapture(1, cv.CAP_V4L2)

ret, frame = cam.read()
if not ret: #null chaining
    print("Can't get camera")
    raise RuntimeError

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #Rrequires graysacale

cv.imshow("img1",gray)

#harrisCount
print("HARRIS")
harrisKeypoiny, harrisTime, harrisMemory, harrisImg = orbBenchMark(gray, scoreType= cv.ORB_HARRIS_SCORE)
cv.imshow("harrisImage", harrisImg)


#fast count
print("FAST")

fastKeypoint, fastTime, fastMemory, fastImg = orbBenchMark(gray, scoreType = cv.ORB_FAST_SCORE)
cv.imshow("fastImage", fastImg)


#wta=2
print("3WTA3")

wta2Keypoints, wta2Time, wta2Memory, wta2Img = orbBenchMark(gray, WTA_K = 2)
cv.imshow("wta2img", wta2Img)



#Wta=3
print("2WTA2")
 
wta3Keypoints, wta3Time, wta3Memory, wta3Img = orbBenchMark(gray, WTA_K = 3)
cv.imshow("wta3img", wta3Img)


while True:
    exitKey= cv.waitKey(0)
    if exitKey == ord('l'):
        cv.destroyAllWindows()
