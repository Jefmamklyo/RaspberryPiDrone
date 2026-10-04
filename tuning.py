import cv2 as cv
import numpy as np

cam1  = cv.VideoCapture(0, cv.CAP_V4L2)


#srtyting resultion
cam1.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cam1.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
cam1.set(cv.CAP_PROP_FPS, 15)



checkerBoardSize = (9,6)
checkerSquareSize = 0.025 #meters

objP = np.zeros((checkerBoardSize[0]*checkerBoardSize[1],3), np.float32)
objP[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1,2)

objP *= checkerSquareSize

objects, images = [],[]



print("Camera 1:",cam1.isOpened())


while True:
        ret1, frame = cam1.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        found, corners = cv.findChessboardCorners(gray, checkerBoardSize)



        display = frame.copy()
        if found:
            cv.drawChessboardCorners( display, checkerBoardSize, corners, found)


        cv.imshow("Original", display)

        key = cv.waitKey(1) & 0xFF

        if key == ord(' ') and found:
            objects.append(objP.copy())
            images.append(corners)

            print(f"Captured {len(objects)}")


        if key == ord('l'):
            break
cam1.release()
cv.destroyAllWindows()

size = gray.shape[::-1]

ret, K, D, rvecs, tvecs = cv.calibrateCamera(objects, images, size, None, None)

fx = K[0,0]
fy = K[1,1]

print("___________________________")
print(f"Focal Lenght X = {fx:.2f}")
print(f"Focal Lenght Y = {fy:.2f}")

