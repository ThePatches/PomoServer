#! /usr/bin/python
"""Client file for the PomoServer."""

from sys import argv, exit

from actions import POM_ACTIONS
from config import *
import pom_msg

if __name__ == '__main__':
    usage = (
        'pom '
        '{start|stop|suspend'
        '|resume|done|repeat|postpone}'
        ' [options]')
    
    try:
        action = POM_ACTIONS[argv[1]]
    except (IndexError, KeyError):
        print usage
        exit(1)

    exit(action(options=argv[1:]))
