from itertools import combinations

def f(x):
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    a = a1 <= x <= a2
    return (a <= p) or q

ans = []
line = [x for x in range(42, 55)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(max(ans))

# otvet: 10
