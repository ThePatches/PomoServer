import SocketServer
import socket
import sys
import threading
import time

import loader
from config import *
from pom_msg import *
from task import Task
from the_work import work_it

class PomHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = fromStr(self.request.recv(1024))
        # self.request.send(response)
        self.request.close()
        self.server.code = data.getCode()
        self.server.msg = data
        if data.getCode() == KILL:
            print 'Shutting down Pom Server...'
            self.server.shutdown()
        elif data.getCode() == SUSPEND:
            print 'Suspending Pom Server...'
        elif data.getCode() == RESUME:
            print 'Resuming the Pom Server...'

    def finish(self):
        self.__done = True

class PServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    daemon_threads = True
    code = RUN             # set indepentendly
    msg = PMsg(RUN, NONE)  # indicates an impending action

if __name__ == "__main__":
    # configure server
    server = PServer((HOST, PORT), PomHandler)

    # begin listening
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    # configure Pomodoro functions
    q = loader.loadFile(FILELOC)
    in_time = time.time()
    isPlay = False
    t_block = WORK_TIME

    print '\nWorking on ' + q[0].name

    while threading.active_count() > 1:
        if len(q.getQue()) == 0 and server.code == RUN:
            print 'No more tasks in queue! Suspending Server'
            server.code = SUSPEND

        if server.code == DONE: #if server.code in [set] use me!
            tasq = work_it(q, server.msg)
            if tasq is not None:
                print 'Starting play time...'
                isPlay = True
                t_block = PLAY_TIME + (WORK_TIME - int(in_time - time.time()))
                in_time = time.time()
            
            server.code = RUN
        elif server.code == RUN:
            if int(time.time() - in_time) > t_block:
                if isPlay == False:
                    tasq = work_it(q, PMsg(DONE, 'None')) # RUN OUT OF TASKS?
                    print 'Starting play time...'
                    isPlay = True
                    t_block = PLAY_TIME
                    in_time = time.time()
                else:
                    print 'Play Time Over...'
                    print 'Begin ' + q[0].name
                    isPlay = False
                    t_block = WORK_TIME
                    in_time = time.time()
        elif server.code == RESUME:
            server.code = RUN
            print  'Resuming Pom Service...' + q[0].name + ' is current task.'
            in_time = time.time()
            isPlay = False
        time.sleep(0.1)
        
    sys.exit(0)

# requires a the_work wrapper function that returns the server to the Run state
