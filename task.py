# import time
from collections import deque

# Task Class

class Task(object):

    def __init__(self, name="none", comment="nada!",
                 recur=False, times=1):
        self.name = name
        self.comment = comment
        self.recur = recur
        self.times = times
        complete = False
        
    def done(self):
        """Mark the task as done."""
        self.complete = True
        if self.recur == True and self.times > 0:
            self.times = self.times - 1
        
class TaskQueue(object):
    
    __thequeue = []

    def __init__(self, ilist):
       self.__thequeue = deque(ilist)

    def __getitem__(self, key):
        return self.__thequeue[key]

    def getQue(self):
        return self.__thequeue

    def mark_complete(self, cont):
        '''mark_complete only does simple completion, not insertion.'''
        t = self.__thequeue.popleft()
        t.done()
        # You will need to generalize this!
        print t.name + ' completed.'
        
        if t.recur == True and t.times != 0:
            if cont == True:
                self.__thequeue.appendleft(t)
            else:
                self.__thequeue.append(t)

        if len(self.__thequeue) != 0: # If there are any items left...
            print self.__thequeue[0].name + ' is up next.'
        else:
            print 'That was the final task!'
        

# TODO: Infinite repeat, move in the queue, delete specific...
