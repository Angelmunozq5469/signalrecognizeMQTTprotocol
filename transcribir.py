from threading import Thread
from queue import Queue

global mensaje
global record
 
mensaje = Queue()
record = Queue()


def start (i):
        while i<10:
                print(i)
                i+=1
        print("Comienzo de cita")
    
    


def stop (i):
        while i<11:
                print(i)
                i+=1
        print("Tu cita finalizo")
        