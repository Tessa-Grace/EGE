from itertools import *
def f(h, l, w, n):
    return (not(h <= l)) <= ((not(w <= n)) and h)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(0, 0, 0, a1), (0, 0, a2, a3), (0, a4, a5, a6)]
    if len(table) == len(set(table)):
        for p in permutations('hlwn'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p)
# otvet: lwnh