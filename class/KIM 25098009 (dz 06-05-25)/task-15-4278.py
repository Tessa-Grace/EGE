def f(x):
    for x in range(1, 10000):
        f = (a % 12 == 0) and (530 % x == 0) <= ((a % x != 0) <= (170 % x != 0))
        if not f:
            return False
    return True

ans = []
for a in range(1, 1000):
    if f(a):
        ans.append(a)
print(len(ans))

# otvet: 16