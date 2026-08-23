import multiprocessing as mp
import cv2 as cv
import numpy as np
import time 


def workerLoop(connection, workFunction): #$connection object and funcito object. Latter takes operation data and returns a computed result

    while True:
        operation = connection.recv()

        if operation is None: #posion pill or somehting like that
            break

        result = workFunction(operation)



        connection.send(result)


    connection.close()


def basicFilteringPipeline(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #gray,, blur gradient
    blur = cv.GaussianBlur(gray, (5,5), 0)
    return blur





prevFrame = 0
currentFrame = 0

if __name__ == '__main__':
    cam = cv.VideoCapture(0, cv.CAP_V4L2)

    parentConnection, childConnection = mp.Pipe()

    process = mp.Process(target = workerLoop, args=(childConnection, basicFilteringPipeline), daemon = True)

    process.start()


    pending = False

    while True:
        ret, frame = cam.read()

        parentConnection.send(frame)

        processedFrame = parentConnection.recv()

        #FRAME RATE
        currentFrame = time.time()
        fps= 1/ (currentFrame - prevFrame)
        prevFrame = currentFrame

        cv.putText(img = processedFrame, text = f"fps:{int(fps)}", org=(7,70), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 3, color = (100, 255, 100), thickness = 2, lineType = cv.LINE_AA)



        cv.imshow("Video",processedFrame)

        if cv.waitKey(1) == ord('l'):
            break




    parentConnection.send(None) #Break the poision pill
    process.join()
    cam.release()
    cv.destroyAllWindows()
