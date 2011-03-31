import time

class Task:
    name = "none"
    comment = "there is nothing about this task..."
    complete = False
    def __init__(self, iName="none", iComment="nada!"):
        self.name = iName
        self.comment=iComment
        complete = False
    def done(self):
        self.complete = True
        

def Demo():
    t = Task("Something")    
    print 'This is something.'
    time.sleep(20)
    print t.name + ' is now done.'
    t.done()
