from pom1 import Task
# This is for parsing tasks 
isTrue = 'T'

def ParseMe(iString):
    # Takes in a string and returns a task
    a = iString.split(',')
    t = Task(a[0], a[1])
    if a[2] == isTrue:
        t.done()
    
    return t
