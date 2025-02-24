from itertools import combinations

def f(x):
    p = 117 <= x <= 158
    q = 129 <= x <= 180
    a = a1 <= x <= a2
    return p <= ((q and not a) <= (not p))

ans = []
line = [x / 10 for x in range(117 * 10, 180 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))

# otvet: 29