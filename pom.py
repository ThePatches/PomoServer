#! /usr/bin/python

import socket
import sys # For command line arguments

# This file interacts with the running service

#-----------CONFIGURATION STUFF----------------

PORT = 12345
HOST = socket.gethostname()

#----------------------------------------------

if sys.argv[1] == '-h':
    f = open('helptext', 'r')
    print f.read()

