'''
Created on Jan 27, 2018

@author: root
'''
from queue import Queue
from threading import Semaphore, BoundedSemaphore

class video_buffer(Queue):
    '''
    Just a wrapper for regular queue with a signalling semaphore
    '''


    def __init__(self, bufferSize):
        '''
        Constructor
        '''
        Queue.__init__(self, bufferSize)
        self.__fullSignalSem = Semaphore(0 - bufferSize)
    
    def dumpWhenFull(self, vlcstream):
        self.__fullSignalSem.acquire(True)
        return super(Queue, self).get(True)
        
        
    def put(self, data):
        super(Queue, self).put(data, True)
        self.__fullSignalSem.release()