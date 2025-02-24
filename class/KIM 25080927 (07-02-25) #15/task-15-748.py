from itertools import combinations

def f(x):
    p = 44 <= x <= 49
    q = 28 <= x <= 53
    a = a1 <= x <= a2
    return ((a <= p) or q)

ans = []
line = [x / 10 for x in range(28 * 10, 53 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(max(ans))

# otvet: 25