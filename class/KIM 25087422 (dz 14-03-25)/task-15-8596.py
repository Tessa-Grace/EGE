def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x >= 11) or (3 * x < y) or (x * y < a)
            if not f:
                return False
    return True

ans = []
for a in range(0, 1000):
    if f(a):
        ans.append(a)
print(min(ans))

# otvet: 301