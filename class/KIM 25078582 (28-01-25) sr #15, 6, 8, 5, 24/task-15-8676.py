def f(B):
    for x in range(0, 1000):
        f = ((x & 500 != 0) and (x & 200 == 0)) <= (not(x & B == 0))
        if not f:
            return False
    return True

ans = []
for B in range(0,1000):
    if f(B):
        ans.append(B)
print(min(ans))

# otvet: 308
