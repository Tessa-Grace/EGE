# 1 method
from itertools import *

def f(w, x, y, z):
    return (z <= (not(y <= x))) or w

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [
        (a1, 1, a2, a3),
        (a4, a5, 0, 0),
        (a6, 0, 1, a7)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p)
# otvet: zyxw

# 2 method
print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (z <= (not(y <= x))) or w
                if not f:
                    print(w, x, y, z)

# w x y z
# 0 0 0 1
# 0 1 0 1
# 0 1 1 1

# otvet: zyxw
