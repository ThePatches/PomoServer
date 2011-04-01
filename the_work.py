#!/usr/bin/env python
from task import Task, TasQue
from loader import loadFile
import time

work_block = 10 * 60
play_block = 2 * 60
# This file does the actual work... Awesome.

def do_pomo():
    #the_que = loadFile('first.dat')
    the_que = TasQue('abc')
    while True: # Set up a loop that does the daemon work
        
        time.sleep(work_block)
        try:
            the_que.mark_complete()
        except:
            pass
        print 'Play Time Begins...'
        time.sleep(play_block)