#!/usr/bin/python
# to do: configuration files? I think so...

from task import Task, TasQue
from pom_msg import *
from loader import loadFile
import time
import socket # my socket info should be parameterized?

port = 12345 # This should be configured
filename = 'first.dat' # should also be configured

work_block = 1 * 60
play_block = 2 * 60
# This file does the actual work... Awesome.

def do_pomo():
    # Time to do some setup...
    the_que = loadFile(filename) # load the work file...
    
    s = socket.socket()
    host = socket.gethostname() # I am me...
    s.bind((host, port))
    s.listen(5)

    t1 = time.time()
    running = True

    while True: # Set up a loop that does the daemon work
        c, addr = s.accept()
        t2 = time.time()
        
        if c != None: # You will need a switch statement here
            msg = fromStr(c.recv(1024))
            if msg.getCode() == KILL: # kill message!
                c.close()
                break
            elif msg.getCode() == SUSPEND: # stop for a bit...
                running = False
            elif msg.getCode() == RESUME: # back in the saddle
                running = True
                t1 = time.time()
            elif msg.getCode() == DONE:
                the_que.mark_complete()
                t1 = time.time()

        print 'Not listening!'

        if running == True:
            print int(t2 - t1)
            if int(t2 - t1) > work_block:
                try:
                    the_que.mark_complete()
                    print 'Work time complete...'
                except:
                    pass

        c.close() # close the connection at the end of this loop.

    s.close()
    print 'Pomo Service Terminated!'

do_pomo()
