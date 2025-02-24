from itertools import *

def f(x, y, z, w):
    return (not w) and ((y or z) <= (y and (not x)))

for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    table = [(a1, a2, a3, 1), (a4, a5, 1, a6), (a7, 1, 1, a8)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p)
# otvet: wzyx