from task import Task, TasQue

# t_list = []
# f = open('first.dat', 'r')
# t_dat = f.read()
# print t_dat
# f.close()

def loadFile(iFile): # Should be a class
    f = open(iFile, 'r')
    tasques = []
    for line in f:
        r = False
        t = 0
        if line[0] != '#':
            s1 = line.split('=')
            s2 = s2.split('|')
            if s2[2] == 'recur':
                r = True
                if s[3] == 'inf':
                    t = -1
                else:
                    t = int(s[3])

            task = Task(s[0], s[1], r, t)
        tasques.append(task)
    q = TasQue(tasques)
