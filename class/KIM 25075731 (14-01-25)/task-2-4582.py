print('w x y z')
for w in range(2):
    for x in 0, 1:
        for y in [0, 1]:
            for z in (0, 1):
                f = not(w <= z)or (x <= y) or not x
                if not f:
                    print(w, x, y, z)

# w x y z
# 0 1 0 0
# 0 1 0 1
# 1 1 0 1
# otvet: wzyx

'''
from itertools import *

def f(w, x, y, z):
    return not(w <= z) or (x <= y) or not x
    
for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, a1, a2, a3), (0, 1, 0, a4), (a5, 0, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
        if [f(**dict(zip(p, r))) for r in table]== [0, 0, 0]:
            print(*p)
'''