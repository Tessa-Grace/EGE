from itertools import combinations

def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = a1 <= x <= a2
    return (not a) <= (b == c)

ans = []
line = [x / 10 for x in range(35 * 10, 111 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))

# otvet: 74