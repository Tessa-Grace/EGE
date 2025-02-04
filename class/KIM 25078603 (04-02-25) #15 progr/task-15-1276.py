from binascii import a2b_qp
from itertools import combinations

def f(x):
    p = 15 <= x <= 33
    q = 35 <= x <= 48
    a = a1 <= x <= a2
    return (a and not q) <= (p or q)

ans = []
line = [x/10 for x in range(14*10, 49*10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(max(ans))

# otvet: 18