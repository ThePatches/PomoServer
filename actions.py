"""Actions for the pomo server client."""

import socket

from config import *
import pom_msg


def start(*args, **kwargs):
    raise NotImplemented

def kill(*args, **kwargs):
    p = pom_msg.PMsg(pom_msg.KILL)
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(p.makeStr())
    s.close()

def done(*args, **kwargs):
    raise NotImplemented

def repeat(*args, **kwargs):
    raise NotImplemented

def postpone(*args, **kwargs):
    raise NotImplemented

def suspend(*args, **kwargs):
    p = pom_msg.PMsg(pom_msg.SUSPEND)
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(p.makeStr())
    s.close()

def resume(*args, **kwargs):
    p = pom_msg.PMsg(pom_msg.RESUME)
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(p.makeStr())
    s.close()
