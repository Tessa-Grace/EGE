def f(a):
    for x in range(1, 100):
        f = (x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0))
        if not f:
            return False
    return True

ans = []
for a in range(1, 1000):
    if f(a):
        ans.append(a)
print(max(ans))

# otvet: 28