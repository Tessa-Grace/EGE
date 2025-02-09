def f(a):
    for x in range(1, 1000):
        f = ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))
        if f:
            return False
    return True

ans = []
for a in range(1, 1000):
    if f(a):
        ans.append(a)
print(min(ans))

# otvet: 2
