# 1 method
from itertools import *

def f(w, x, y, z):
    return not(w <= (x == y)) and (z <= x)

for a1, a2, a3, a4, a5 in product([0,1], repeat=5):
    table = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p)
# otvet: yxwz

# 2 method
print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = not(w <= (x == y)) and (z <= x)
                if f:
                    print(w, x, y, z)
# w x y z
# 1 0 1 0
# 1 1 0 0
# 1 1 0 1

# otvet: yxwz


