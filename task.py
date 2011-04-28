""" Pomo Task Related classes. """

from collections import deque

class Task(object):
    """ Class that holds information about a task. """
    
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
    """ Holds a block of tasks. """

    __thequeue = []

    def __init__(self, ilist = []):
       self.__thequeue = deque(ilist)

    def __getitem__(self, key):
        return self.__thequeue[key]

    def getQue(self):
        """ Returns the queue, in case you need it. """
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
        
    def to_file(self, filename):
    	""" Writes the task list to the specified file """
        f = open(filename, 'w')
        for x in self.__thequeue:
            line = []
            line.append(x.name)
            line.append(x.comment)
            if x.recur:
                line.append('recur')
                if x.times == -1:
                    line.append('inf')
                else:
                    line.append(str(x.times))
            else:
                line.append('once')

            o_line = '|'.join(line)
            o_line = 'task=' + o_line + '\n'
            f.write(o_line)
            del line

    def from_file(self, filename):
        """ Loads a TaskQueue from a file File Name """
        f = file(filename)
        task_queues = []
        task = Task('empty', 'nothing')
        for line in f:
            line = line.strip()
            r = False
            t = 0
            if not line.startswith('#'):
                s1 = line.split('=')
                s2 = s1[1].split('|')
                if s2[2].strip() == 'recur':
                    r = True
                    if str(s2[3])[:3].strip() == 'inf':
                        t = -1
                    else:
                        t = int(s2[3])
                task = Task(s2[0], s2[1], r, t)
                task_queues.append(task)
        f.close()
        self.__thequeue = deque(task_queues)
