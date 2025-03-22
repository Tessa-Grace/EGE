from itertools import *

def f(w, x, y, z):
    return (not x or y or not z or w) and not(not x or w)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (a1, 0, a2, 1),
        (0, a3, 0, a4),
        (1, 0, 0, a5)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p)

# otvet: ywzx
