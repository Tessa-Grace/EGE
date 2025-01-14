from itertools import *

def f1(w, x, y, z):
    return (w == x) and (y <= z)

def f2(w, x, y, z):
    return (w <= x) <= (y == x)

for a1, a2, a3, a4, a in product([0, 1], repeat=5):
    table= [
        (1, a1, 1, 1),
        (a2, 1, 0, 0),
        (a3, 0, 0, a4)
    ]
    for p in permutations('wxyz'):
        if [f1(**dict(zip(p, r))) for r in table] == [1, 1, 0] and \
                [f2(**dict(zip(p, r))) for r in table] == [1, 1, 0] == [0, 1, 0]:
            print(*p)
