from itertools import *

def f(w, x, y, z):
    return (x or not y) and not(x == z) and w

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, 0, 0, 1), (0, 0, 1, 1), (0, a2, a3, a4)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
# ('z', 'y', 'x', 'w')
# otvet: zyxw
