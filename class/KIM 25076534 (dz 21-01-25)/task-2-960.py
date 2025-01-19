from itertools import *

def f(a, b, c):
    return a and not b or c

table = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]
for p in permutations('abc'):
    if [f(**dict(zip(p, t))) for t in table] == [0, 1, 1, 1, 0, 0, 1, 1]:
        print(*p)
# otvet: bca