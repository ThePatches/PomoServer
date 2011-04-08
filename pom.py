#! /usr/bin/python

import socket
import sys # For command line arguments
import pom_msg
from config import *

# This file interacts with the running service

def doSending(msg):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(msg.makeStr())
    s.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            f = open('helptext', 'r')
            print f.read()
        elif sys.argv[1] == '-k':
            p = pom_msg.PMsg(pom_msg.KILL)
            doSending(p)
        elif sys.argv[1] == '-s':
            p = pom_msg.PMsg(pom_msg.SUSPEND)
            doSending(p)
        elif sys.argv[1] == '-e':
            p = pom_msg.PMsg(pom_msg.RESUME)
            doSending(p)
        elif sys.argv[1] == '-d':
            p = pom_msg.PMsg(pom_msg.DONE)
            doSending(p)
        else:
            print 'Nothing to do.'
    else:
        print "Invalid option! Use '-h' for a list of arguments."

