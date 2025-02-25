from itertools import *

def f(x, y, z, w):
    return not w and z and (y <= x)

table = [(1, 0, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1)]

for p in permutations('xyzw'):
    if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
        print(p)

#>>>('z', 'w', 'x', 'y')     