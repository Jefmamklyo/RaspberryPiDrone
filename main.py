import multiprocessing as mp
import cv2
import numpy as np
from dataclasses import dataclass

@dataclass
class Result:
    value: object

def workerLoop(connection, workFunction): #$connection object and funcito object. Latter takes operation data and returns a computed result
    """
    Connection is the global bariable taht is the only acces point into this funciton
    operation take the connection where connection.recv() recieves the object sent by another using send(obj)
    This funcitons code executes inside the new adn spawned process aka a new core bypassing pypthon interpereter

    
    """
    while True:
        operation = connection.recv()

        if operation is None: #posion pill or somehting like that
            break

        result = function(operation)



        connection.send()


    connection.close()



class ProcessWorker:
    def __init__(self, workFunction):
        self.workFunction = workFunction
        self.parentConnection = None
        self.process = None
    
    #Context manager
    def __enter__(self):
        self.parentConnection, childConnection = mp.Pipe()

        self.process = mp.Process(target = workerLoop, args=(childConnection, self.workFunction), daemon = True)
        
        self.process.start()

        return self


    def __exit__(self): #Sends none to cancel the worker loops recursive usage
        self.parentConnection.send(None)
        self.process.join() #Bl;pookcs exectionof main program iuntil process function finished its process

    def dispatch(self, operation):
        self.parentConnection.send(operation)


