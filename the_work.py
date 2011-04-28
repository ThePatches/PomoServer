#!/usr/bin/python

from config import *
from loader import loadFile
from task import *
from pom_msg import *

def work_it(tasks, msg):
    """ Does task manipulation within the queue. """
    if msg.getCode() == DONE:
        print 'Completed ' + tasks[0].name
        if msg.getAction() == NONE:
            tasks.mark_complete(False)
        elif msg.getAction()[:6] == RECR:
            n = int(msg.getAction().split(' ')[1])
            if tasks[0].recur == False:
                tasks[0].recur = True
                tasks[0].times = 1 + n
            else:
                tasks[0].times + n
            tasks.mark_complete(True)
        elif msg.getAction()[:6] == DELAY: # poor style...
            n = int(msg.getAction().split(' ')[1])
            if tasks[0].recur == False:
                tasks[0].recur = True
                tasks[0].times = 1 + n
            else:
                tasks[0].times + n
            tasks.mark_complete(False)
        else:
            print 'Action not supported...'

    if len(tasks.getQue()) != 0:
        return tasks[0]
    else:
        return None
    

# for testing purposes
if __name__ == "__main__":
    q = loadFile(FILELOC)
    mesg = PMsg(DONE, DELAY + '1')

    work_it(q, mesg)

    print q[0].name + ' ' + str(q[0].times)

