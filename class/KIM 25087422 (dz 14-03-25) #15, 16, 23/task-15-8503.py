def f(a):
    for x in range(0, 1000):
        f = (((x & 52 != 0) and (x & 36 == 0)) <= (not(x & a == 0)))
        if not f:
            return False
    return True

ans = []
for a in range(0, 1000):
    if f(a):
        ans.append(a)
print(min(ans))

# otvet: 16