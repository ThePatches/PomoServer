# import time
from collections import deque

# Task Class

class Task:
    name = "none"
    comment = "there is nothing about this task..."
    complete = False
    recur = False
    times = 1
    def __init__(self, iName="none", iComment="nada!",
                 iRecur=False, iTimes=1):
        self.name = iName
        self.comment=iComment
        complete = False
        self.recur = iRecur
        self.times = iTimes
        
    def done(self):
        self.complete = True
        if self.recur == True and self.times > 0:
            self.times = self.times - 1
        
# Task Queue?
class TasQue:
    __thequeue = []

    def __init__(self, ilist):
        __thequeue = deque(ilist)

 # mark_complete only does simple completion, not insertion
    def mark_complete(self, cont):
        t = __thequeue.popleft()
        t.done()
        if t.recur == True and t.times != 0:
            if cont == True:
                __thequeue.appendleft(t)
            else:
                __thequeue.append(t)
        

# TODO: Infinite repeat, move in the queue, delete specific...
