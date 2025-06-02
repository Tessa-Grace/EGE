from itertools import *

def f(w, x, y, z):
    return x and (z <= w) and not y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [
        (a1, a2, 1, a3),
        (a4, 1, 0, a5),
        (1, 0, a6, a7)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p)

# otvet: xwzy