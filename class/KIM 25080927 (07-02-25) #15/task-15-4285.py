from itertools import combinations

def f(x):
    p = 25 <= x <= 240
    q = 175 <= x <= 300
    r = 270 <= x <= 340
    a = a1 <= x <= a2
    return (q <= p) or ((not a) <= r)

ans = []
line = [x / 10 for x in range(25 * 10, 340 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))

# otvet: 30