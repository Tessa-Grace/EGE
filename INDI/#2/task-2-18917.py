from itertools import *

def f(t, s, r, a):
    return (s or not r) and not(r == a) and t

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 1, a1, 0), (a2, 1, 1, 0), (1, a3, 0, a4)]
    if len(table) == len(set(table)):
        for p in permutations('tsra'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
# ('s', 't', 'a', 'r')
# otvet: star