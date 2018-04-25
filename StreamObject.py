'''
Created on Jan 23, 2018

@author: root
'''
from queue import Queue

class StreamObject():
    '''
    classdocs
    '''
    QUEUE_SIZE = 1000000
    QUEUE_RW_BLOCK_TIMEOUT = 10000

    def __init__(self):
        '''
        Constructor
        '''
        self.__queue = Queue(self.QUEUE_SIZE)
        self.numberOfBytesWritten = 0
        
    def write(self, bytesLikeObject):
        self.__queue.put(bytesLikeObject, True, self.QUEUE_RW_BLOCK_TIMEOUT)
        self.numberOfBytesWritten += len(bytesLikeObject)
        return len(bytesLikeObject)
    
    def read(self):
        return self.__queue.get(True, self.QUEUE_RW_BLOCK_TIMEOUT)
    
    def printBytes(self):
        print("Bytes written:"+ str(self.numberOfBytesWritten))