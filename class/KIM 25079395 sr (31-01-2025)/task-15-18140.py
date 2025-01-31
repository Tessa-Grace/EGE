def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x * y >= 39) or (y <= x) or ( y >= A - 20)
            if not f:
                return False
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

# otvet: 22