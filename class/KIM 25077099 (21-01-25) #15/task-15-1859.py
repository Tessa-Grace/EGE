def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (2 * x + y != 70) or (x < y) or (A < x)
            if not f:
                return False
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

# otvet: 23