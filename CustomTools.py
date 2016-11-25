import random
def mode():
    mode = input("direction")
    if mode == "U":
        axis = 1
    if mode == "D":
        axis = 2
    if mode == "L":
        axis = 3
    if mode == "R":
        axis = 4
    return axis

def transpose(a):
    a = [list(i) for i in zip(*a)]
    return a

def CustomSort(a, axis):
    e = []
    t = 0
    while t < 4:
        b = []
        for item in a[t]:
            b.append(item)
        if axis == 3 or axis == 1:
            b.sort(key=bool, reverse=True)
        else:
            b.sort(key=bool)
        e.append([b])
        t = t + 1
    return e

def GridPrint(a):
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])

def score(a):
    e = []
    t = 0
    while t < 4:
        for item in a[t]:
            e.append(item)
        t = t + 1
    e = sum(e)
    return e

def MergeLogic(a):
    a0 = a[0]
    a1 = a[1]
    a2 = a[2]
    a3 = a[3]
    e = []
    z = 3
    while z > -1:
        t = int(z - 1)
        if a0[z] == a0[t]:
            a0[z] = int(a0[t] * 2)
            a0[t] = 0
        if a1[z] == a1[t]:
            a1[z] = int(a1[t] * 2)
            a1[t] = 0
        if a2[z] == a2[t]:
            a2[z] = int(a2[t] * 2)
            a2[t] = 0
        if a3[z] == a3[t]:
            a3[z] = int(a3[t] * 2)
            a3[t] = 0
        z = int(z - 1)
    e.append([a0])
    e.append([a1])
    e.append([a2])
    e.append([a3])
    return e

def TileSpawn(a):
    b = random.choice([2, 4])
    c = random.randrange(0, 3)
    d = random.randrange(0, 3)
    e = a[c]
    while e[d] != 0:
        c = random.randrange(0, 3)
        d = random.randrange(0, 3)
    e[d] = b
    a[c] = e
    return a

def TileSpawnInit(a):
    c = random.randrange(0, 3)
    d = random.randrange(0, 3)
    e = a[c]
    while e[d] != 0:
        c = random.randrange(0, 3)
        d = random.randrange(0, 3)
    e[d] = 2
    a[c] = e
    return a
