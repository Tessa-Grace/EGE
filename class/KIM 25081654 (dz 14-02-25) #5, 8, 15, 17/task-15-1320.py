from itertools import combinations

def f(x):
    p = 10 <= x <= 25
    q = 15 <= x <= 30
    r = 25 <= x <= 40
    a = a1 <= x <= a2
    return (q <= (not r)) and a and not p

ans = []
line = [x / 10 for x in range(10 * 10, 41 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) == 0 for x in line):
        ans.append(a2 - a1)
print(max(ans))

# otvet: 20