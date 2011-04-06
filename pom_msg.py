#! /usr/bin/python

# message class and messages
# useless because of string passing?

RUN = -1
KILL = 0
SUSPEND = 1
RESUME = 2
DONE = 3

class PMsg:
    __code = 0
    __action = 'None'

    def __init__(self, icode = 0, iaction='None'):
        self.__code = icode
        self.__action = iaction

    def isSimple(self):
        """ Determines whether the action is simple... """
        if (self.__code == KILL or self.__code == SUSPEND or
            self.__code == RESUME):
            return True
        else:
            return False
    
    def getAction(self):
        if self.isSimple() != True:
            return self.__action
        else:
            return 'simple'

    def getCode(self):
        return self.__code

    def makeStr(self):
        return str(self.__code) + '|' + self.__action

def fromStr(iString):
    arr = iString.split('|')
    return PMsg(int(arr[0]), arr[1])
