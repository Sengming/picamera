'''
Created on Jan 23, 2018

@author: root
'''
from queue import Queue

class StreamObject():
    '''
    classdocs
    '''
    QUEUE_SIZE = 10000
    QUEUE_RW_BLOCK_TIMEOUT = 10000

    def __init__(self):
        '''
        Constructor
        '''
        self.__queue = Queue(self.QUEUE_SIZE)
        
    def write(self, bytesLikeObject):
        self.__queue.put(bytesLikeObject, True, self.QUEUE_RW_BLOCK_TIMEOUT)
        return len(bytesLikeObject)
    
    def read(self):
        return self.__queue.get(True, self.QUEUE_RW_BLOCK_TIMEOUT)