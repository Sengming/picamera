'''
Created on Jan 23, 2018

@author: root
'''
from IStreamSubscriber import IStreamSubscriber

class UartSubscriber(IStreamSubscriber):
    '''
    '''
#     def __init__(self):
#         '''
#         Constructor
#         '''
#         pass
    
    def __init__(self):
        self.__canOutputData = True
    
    def output(self, data):
        '''
        Prints out byte data to stdout for debug purposes
        '''
#         if (self.__canOutputData):
#             print(data)
        
    def allowOutput(self):
        self.__canOutputData = True
    
    def disableOutput(self):
        self.__canOutputData = False