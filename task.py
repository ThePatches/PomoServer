# import time
from collections import deque

# Task Class

class Task(object):

    def __init__(self, iName="none", iComment="nada!",
                 iRecur=False, iTimes=1):
        self.name = iName
        self.comment=iComment
        complete = False
        self.recur = iRecur
        self.times = iTimes
        
    def done(self):
        """Mark the task as done."""
        self.complete = True
        if self.recur == True and self.times > 0:
            self.times = self.times - 1
        
# Task Queue?
class TasQue(object):
    __thequeue = []
    def __init__(self, ilist):
       self.__thequeue = deque(ilist)

    def __getitem__(self, key):
        return self.__thequeue[key]

    def getQue(self):
        return self.__thequeue

 # mark_complete only does simple completion, not insertion
    def mark_complete(self, cont):
        t = self.__thequeue.popleft()
        t.done()
        # You will need to generalize this!
        print t.name + ' completed.'
        print self.__thequeue[0].name + ' is up next.'
        if t.recur == True and t.times != 0:
            if cont == True:
                self.__thequeue.appendleft(t)
            else:
                self.__thequeue.append(t)
        

# TODO: Infinite repeat, move in the queue, delete specific...
