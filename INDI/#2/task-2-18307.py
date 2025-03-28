from itertools import *

def f(a, b, c, d):
    return ((a or b) <= (not c and a)) and d

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(1, 1, a1, 1), (1, a2, 1, a3), (a4, a5, a6, 1)]
    if len(table) == len(set(table)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
# ('d', 'b', 'c', 'a')
# otvet: dbca