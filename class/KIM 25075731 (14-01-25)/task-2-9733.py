from itertools import *

def f(w, x, y, z):
    return (x and not y) or (x == z) or w

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, a2, 0, 1), (1, 0, a3, 1), (1, 1, 0, a4)]
    for p in permutations('wxyz'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(*p)

#otvet: y x w z