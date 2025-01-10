from itertools import *

def f(w, x, y, z):
    return not(w <= (x == y)) and (z <= x) # y or y - это просто y

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
# ('y', 'x', 'w', 'z')
# otvet: yxwz