from itertools import *

def f(w, x, y, z):
    return (y <= x) and not z and w

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
    table = [(1, 0, a1, a2), (1, 1, a3, a4), (a5, 1, 1, a6)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p)
# otvet: wyxz