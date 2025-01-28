def f(A):
    for x in range(1, 1000):
        for d in range(1, 1000):
            f = ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)
            if not f:
                return False
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

# otvet: 390
