import multiprocessing as mp
import cv2 as cv
import numpy as np


def workerLoop(connection, workFunction): #$connection object and funcito object. Latter takes operation data and returns a computed result

    while True:
        operation = connection.recv()

        if operation is None: #posion pill or somehting like that
            break

        result = function(operation)



        connection.send(result)


    connection.close()


def basicFilteringPipeline(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #gray,, blur gradient
    blur = cv.GaussianBlur(gray, (5,5), 0)
    return blur





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

        cv.imShoow("Video",processedFrame)

        if cv.waitKey(1) == ord('l'):
            break




    parentConnection.send(None) #Break the poision pill
    process.join()
    cam.release()
    cv.destroyAllWindows()
