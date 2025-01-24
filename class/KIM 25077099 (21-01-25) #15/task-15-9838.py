def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x + 2 * y > A) or (y < x) or (x < 30)
            if not f:
                return False
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

# otvet: 89