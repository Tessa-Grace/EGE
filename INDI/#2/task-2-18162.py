from itertools import *

def f(a, b, c, d):
    return ((a <= b) == c) or d

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(1, 0, 1, a1), (1, 0, a2, 1), (a3, a4, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, r))) for r in table] == [0,  0, 0]:
                print(*p)
# otvet: adbc