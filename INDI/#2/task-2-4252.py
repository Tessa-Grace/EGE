from itertools import *

def f(w, x, y, z):
    return z or ((w or not y) == (x <= z))

table = [(0, 1, 0, 0), (0, 0, 1, 1), (0, 0, 1, 0)]

for p in permutations('wxyz'):
    if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
        print(p)

#>>>('z', 'y', 'x', 'w')      