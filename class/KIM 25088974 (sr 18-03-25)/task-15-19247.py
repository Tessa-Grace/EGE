def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - 3 * y  < A) or (y > 400) or (x > 56)
            if not f:
                return 0
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(min(ans))

# otvet: 54