from itertools import combinations

def f(x):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2
    return (a <= r) and ((not(a <= p)) <= q)

ans = []
line = [x + eps for x in range(5, 259) for eps in [0, 0.1, 0.9]]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))

# otvet: 0