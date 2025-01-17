from itertools import *

def f(w, x, y, z):
    return (z and not w) or (z == x) or y

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, a2, 0, 1), (1, 0, a3, 1), (1, 1, 0, a4)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p)

# otvet: wzyx
