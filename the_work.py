#!/usr/bin/python
# to do: configuration files? I think so...

from task import Task, TasQue
from loader import loadFile
import time
import socket # my socket info should be parameterized?

port = 12345 # This should be configured
filename = 'first.dat' # should also be configured

work_block = 10 * 60
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

    while True: # Set up a loop that does the daemon work
        c, addr = s.accept()
        msg = c.recv(1024)
        t2 = time.time()
        
        if c != None:
            if msg == 0: # kill message!
                break

        if int(t2 - t1) > work_block:
            try:
                the_que.mark_complete()
                print 'Work time complete...'
            except:
                pass

        c.close() # close the connection at the end of this loop.
        # time.sleep(play_block)

    print 'Pomo Service Terminated!'
