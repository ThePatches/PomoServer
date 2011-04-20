"""Pomodoro message tools"""

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

    def __init__(self, code = 0, action='None'):
        self.__code = code
        self.__action = action

    def isSimple(self):
        """ Determines whether the action is simple... """
        return(self.__code == KILL or
            self.__code == SUSPEND or
            self.__code == RESUME)
    
    def getAction(self):
        if not self.isSimple():
            return self.__action
        else:
            return 'simple'

    def getCode(self):
        return self.__code

    def makeStr(self):
        return str(self.__code) + '|' + self.__action

def fromStr(msg_str):
    arr = msg_str.split('|')
    return PMsg(int(arr[0]), arr[1])
