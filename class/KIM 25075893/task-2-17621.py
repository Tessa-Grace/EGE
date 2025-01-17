# 1 method

from itertools import *

def f(w, x, y, z):
    return not(x <= z) or (y == w) or y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, 0, a1, a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p)
# otvet: zxyw

# 2 method
print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = not(x <= z) or (y == w) or y
                if not f:
                    print(w, x, y, z)
# w x y z
# 1 0 0 0
# 1 0 0 1
# 1 1 0 1

# otvet: zxyw


