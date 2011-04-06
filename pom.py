#! /usr/bin/python

import socket
import sys # For command line arguments
import pom_msg

# This file interacts with the running service

#-----------CONFIGURATION STUFF----------------

PORT = 12345
HOST = "localhost"

#----------------------------------------------

if len(sys.argv) > 1:
    if sys.argv[1] == '-h':
        f = open('helptext', 'r')
        print f.read()
    elif sys.argv[1] == '-k':
        p = pom_msg.PMsg(pom_msg.KILL)
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(p.makeStr())
        s.close()
    else:
        print 'Nothing to do.'
else:
    print "Invalid option! Use '-h' for a list of arguments."

