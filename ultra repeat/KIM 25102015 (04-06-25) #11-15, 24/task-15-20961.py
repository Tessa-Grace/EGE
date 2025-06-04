#20961

from itertools import combinations

def f(x):
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    a = a1 <= x <= a2
    return ((q <= (((not a) and p) <= (not q))))

ans = []
line = [x + eps for x in range(15, 168) for eps in [0, 0.1, 0.9]]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))

# otvet: 104