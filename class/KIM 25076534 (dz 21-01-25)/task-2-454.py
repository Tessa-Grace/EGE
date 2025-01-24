from itertools import *

def f(a, b, c, d):
    return not(b <= a) and (c <= d) or a and b and c and not d

for a1, a2, a3, a4, a5, a6, a7, a8, a9 in product([0, 1], repeat=9):
    table = [
        (a1, 0, 0, 0),
        (a2, a3, a4, 0),
        (a5, a6, 0, 0),
        (a7, 0, a8, a9)
    ]
    if len(table) == len(set(table)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]:
                print(*p)
# otvet: bdca