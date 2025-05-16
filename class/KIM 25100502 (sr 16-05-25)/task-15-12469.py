from itertools import combinations

def f(x):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    a = a1 <= x <= a2
    return (d <= (not c and not a)) <= (not d)

ans = []
line = [x / 10 for x in range(7 * 10, 101 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))

# otvet: 22