import multiprocessing as mp
import queue
import cv2 as cv
import numpy as np
import time 


def workerLoop(operationQueue, resultQueue, workFunction): #$connection object and funcito object. Latter takes operation data and returns a computed result

    while True:
        operation = operationQueue.get()
        

        if operation is None: #Sentinental Value 
            break


        try:
            result = workFunction(operation)
        except Exception as e:
            print(f" Frame is not being processeed {e}")
            pass

        resultQueue.put(result)


def basicFilteringPipeline(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #gray,, blur gradient
    blur = cv.GaussianBlur(gray, (5,5), 0)
    return blur





prevFrame = 0
currentFrame = 0

if __name__ == '__main__':
    cam = cv.VideoCapture(0, cv.CAP_V4L2)

    #initlisie queses
    operationQueue = mp.Queue(maxsize=1)
    resultQueue = mp.Queue(maxsize = 1) #Raises queue.FUll

    #args is arguments required in the argument function to be passed in
    process = mp.Process(target = workerLoop, args=(operationQueue, resultQueue, basicFilteringPipeline), daemon = True)

    process.start()


    while True:
        ret, frame = cam.read()

        if not ret:
            break

        #try execpt hjandle put and get full. Sends to the worker fucntiuon
        try: 
            operationQueue.put_nowait(frame)
        except queue.Full: 
            print("Queue ios full raised full exception")

        #RECIEVES FROM WORKER FUNCTION
        try:
            processedFrame = resultQueue.get_nowait()

            #Main
            currentFrame = time.time()
            fps= 1/ (currentFrame - prevFrame)
            prevFrame = currentFrame
            
            cv.putText(img = processedFrame, text = f"fps:{int(fps)}", org=(7,70), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 3, color = (100, 255, 100), thickness = 2, lineType = cv.LINE_AA)


            cv.imshow("Frame", processedFrame)

            
        except queue.Empty:
            print("Queue is emplty")

        
        if not process.is_alive:
            print("Processes isn';t alive will terminate")
            break


        if cv.waitKey(1) == ord('l'):
            break



    operationQueue.put(None) #Send sentinental value
    process.join()
    cam.release()
    cv.destroyAllWindows()

operationQueue.put(None) #Send sentinental value
process.join()
cam.release()
cv.destroyAllWindows()
