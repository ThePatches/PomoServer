import SocketServer
import socket
import sys
import threading
import time

from config import *
from pom_msg import *
from task import Task, TaskQueue
from the_work import work_it
import prctl

class PomHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = fromStr(self.request.recv(1024))
        self.request.close()
        self.server.code = data.getCode()
        self.server.msg = data
        
        # Server operations are handled here...
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
    
    def SetUp(self):
        """ Creates instance level variables for code and message. """
        self.code = RUN
        self.msg = PMsg(RUN, NONE)

def main():
    # configure server
    server = PServer((HOST, PORT), PomHandler)
    server.SetUp()
    prctl.set_name('PomoServer')
    prctl.set_proctitle('PomoServer')

    # begin listening
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    # configure Pomodoro functions
    q = TaskQueue()
    q.from_file(FILELOC)
    in_time = time.time() # When the block started
    isPlay = False
    t_block = WORK_TIME   # Size of the block we are in
    suspend_ticks = 0     # The ticks elapsed before suspension

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
            if int(time.time() - in_time) > t_block - suspend_ticks:
                suspend_ticks = 0
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
        elif server.code == CURRENT:
            print 'Current task: ' + q[0].name
            server.code = RUN
        elif server.code == SUSPEND:
            suspend_ticks = in_time - time.time()
        
        time.sleep(0.1)

    q.to_file(FILELOC)
    sys.exit(0)
    
if __name__ == "__main__":
    main()
