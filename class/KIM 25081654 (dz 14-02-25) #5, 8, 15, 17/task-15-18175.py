def f(a):
    for x in range(1, 1000):
        f = ((x % 7 != 0) and (x % 13 == 0)) <= (x > a - 40)
        if not f:
            return False
    return True

ans = []
for a in range(1, 1000):
    if f(a):
        ans.append(a)
print(max(ans))

# otvet: 52