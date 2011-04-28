"""Pomodoro message tools"""

import socket

from config import *

# Numeric Codes for operation
RUN = -1
KILL = 0
SUSPEND = 1
RESUME = 2
DONE = 3
CURRENT = 4

# some constants
RECR = 'RECUR ' # indicates a recurring task. Format: RECUR X <- X = num times
NONE = 'None'   # Blank Task based only on its codes
DELAY = 'DELAY '# indicates a task delayed to later in the list Format: DELAY X <- X = num times 

class PMsg(object):
    """ Class for passing Pomodoro Messages to the Server """

    def __init__(self, code = 0, action='None'):
        self.__code = code
        self.__action = action

    def isSimple(self):
        """ Determines whether the action is simple... """
        return(self.__code == KILL or
            self.__code == SUSPEND or
            self.__code == RESUME)
    
    def getAction(self):
        """ Returns the action if the message is simple, the string 'simple'
if it is not. """
        if not self.isSimple():
            return self.__action
        else:
            return 'simple'

    def getCode(self):
        """ Get's the message's code value. """
        return self.__code

    def makeStr(self):
        """ Converts the message into a string.
Required for sending to the sever. """
        return str(self.__code) + '|' + self.__action

def fromStr(msg_str):
    """ Gets a PMsg object from a string. """
    arr = msg_str.split('|')
    return PMsg(int(arr[0]), arr[1])

def sendMessage(msg):
    """ Sends a message to the PomoSever using the defined HOST and PORT values. """
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(msg.makeStr())
    s.close()
