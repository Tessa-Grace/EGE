from itertools import *

def f(w, x, y, z):
    return ((x <= z) <=y) or not w

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, 0, a1, a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p)
# otvet: z x y w
