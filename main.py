import multiprocessing as mp
import cv2
import numpy as np
import time

def workerLoop(connection, function): #$connection object and funcito object. Latter takes task data and returns a computed result
    while True:
        task = connection.recv()

        if task is None: #posion pill or somehting like that
            break

        start = time.perf_counter() # to calculate thge time