'''
Created on Jan 23, 2018

@author: root
'''
from IStreamSubscriber import IStreamSubscriber
import sys

class DebugSubscriber(IStreamSubscriber):
    '''
    Debug output subscriber
    '''
    def __init__(self):
        self.__canOutputData = True
    
    def output(self, data):
        '''
        Prints out byte data to stdout for debug purposes
        '''
        if self.__canOutputData is True:
            sys.stdout.buffer.write(data)
            sys.stdout.flush()
            return
        
    def allowOutput(self):
        self.__canOutputData = True
    
    def disableOutput(self):
        self.__canOutputData = False