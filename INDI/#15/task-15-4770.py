from itertools import combinations

def f(x):
    p = 35 <= x <= 55
    q = 45 <= x <= 65
    a = a1 <= x <= a2
    f1 = p <= a
    f2 = (not a) <= (not q)
    return f1 == f2

ans = []
line = [x / 10 for x in range(35 * 10, 66 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))

# otvet: 30