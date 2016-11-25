import itertools
import CustomTools as f
import random

a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
a = f.TileSpawnInit(a)
a = f.TileSpawnInit(a)
f.GridPrint(a)
while 1 == 1:
    axis = int(input("1 for up, 2 for down, 3 for left, 4 for right"))
    if axis < 3:
        a = f.transpose(a)
    b = f.CustomSort(a, axis)
    a = list(itertools.chain.from_iterable(b))
    b = f.MergeLogic(a)
    a = list(itertools.chain.from_iterable(b))
    b = f.CustomSort(a, axis)
    a = list(itertools.chain.from_iterable(b))
    a = f.TileSpawn(a)#easily the worst part of the code but haven't found a way to streamline
    if axis < 3:
        a = f.transpose(a)
    f.GridPrint(a)
    score = f.score(a)
    print("score =", score)
