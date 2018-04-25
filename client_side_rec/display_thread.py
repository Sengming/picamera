'''
Created on Jan 27, 2018

@author: root
'''
import threading
from time import sleep


class DisplayThread(threading.Thread):
    '''Reads the byte stream sent and broadcasts to subscribers'''
    def __init__(self, playerSubprocess, queue, qMaxSize, socket):
        threading.Thread.__init__(self)
        self.__subscribers = []
        self.__playerSubprocess = playerSubprocess
        self.__queue = queue
        self.__queueMaxSize = qMaxSize
        self.__clientSocket = socket

    def run(self):
#         for i in range()
#             self.__playerSubprocess.stdin.write(data)
#             print(data)
        while True:
            self.__clientSocket.send(b'0101')
            print("Poll server")
            sleep(0.5)
                    
        
        