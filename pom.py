#! /usr/bin/python
"""Client file for the PomoServer."""

import optparse

from actions import (
    done,
    kill,
    postpone,
    repeat,
    resume,
    suspend,
    )

from config import *
import pom_msg

def main():
    usage = 'pom [options]'
    parser = optparse.OptionParser(usage=usage)

    parser.add_option('-k', '--kill', 
        help='Kill the service.',
        action='callback', callback=kill)
    parser.add_option('-d', '--done', 
        help='Mark the current task finished.',
        action='callback', callback=done)
    parser.add_option('-r', '--repeat', 
        help='Repeat the current task.',
        action='callback', callback=repeat)
    parser.add_option('-p', '--postpone',
        help='Postpone task by moving to the end of the queue.',
        action='callback', callback=postpone)
    parser.add_option('-s', '--suspend', 
        help='Suspend the service.',
        action="callback", callback=suspend)
    parser.add_option('-e', '--resume',
        help='Resume the service if suspended.',
        action="callback", callback=resume)

    (options, args) = parser.parse_args()

def doSending(msg):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(msg.makeStr())
    s.close()

if __name__ == '__main__':
    main()
