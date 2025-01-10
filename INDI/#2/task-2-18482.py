from itertools import *

def f(x, y, z, w):
    return (x == (y <= (z or x))) and w

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, 0, 1, a1), (0, a2, a3, 0), (1, 0, a4, a5)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
# ('x', 'y', 'w', 'z')
# otvet: xywz
