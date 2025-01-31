def f(A):
    for x in range(1, 1000):
        f = (x & 57 == 0) or ((x & 23 == 0) <= (not(x & A == 0)))
        if not f:
            return False
    return True

ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(min(ans))

# otvet: 40