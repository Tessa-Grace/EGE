from itertools import *

def f(w,x,y, z):
    return (w or y) and (x <= (not z)) and not w

ans = []
for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (a1, 0, a2, 0),
        (1, a3, a4, a5),
        (1, 1, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                ans.append(p)

print(len(set(ans)))