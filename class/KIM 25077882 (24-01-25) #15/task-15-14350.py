def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = not((x < 7) or (y >= 3 * x + A - 20) or (x >= 34) or (y < 121))
            if f:
                return False
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

# otvet: 42