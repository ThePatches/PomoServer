from task import Task, TasQue

# t_list = []
# f = open('first.dat', 'r')
# t_dat = f.read()
# print t_dat
# f.close()

def loadFile(iFile): # Should be a class
    f = open(iFile, 'r')
    tasques = []
    task = Task('empty', 'nothing')
    for line in f:
        r = False
        t = 0
        if line[0] != '#':
            s1 = line.split('=')
            s2 = s1[1].split('|')
            if s2[2] == 'recur':
                r = True
                if str(s2[3])[:3] == 'inf':
                    t = -1
                else:
                    t = int(s2[3])
            task = Task(s2[0], s2[1], r, t)
        tasques.append(task)
    f.close()
    q = TasQue(tasques)
    return q
