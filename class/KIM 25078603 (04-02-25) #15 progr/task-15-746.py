from itertools import combinations

def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [x for x in range(11, 55)] # крайние значения с запасом
for A1, A2 in combinations(line, 2): # (11, 12), (11, 13), (11, 14) и тд
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

# otvet: 23
