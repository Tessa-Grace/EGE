from itertools import combinations

def f(x):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = a1 <= x <= a2
    return (p == q) <= (not a)

ans = []
line = [x/10 for x in range(4*10, 32*10)]
# работа генератора выше /
# [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 ...]
# [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0 ...]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(max(ans))

# 8.9 ~ 9
# otvet: 9