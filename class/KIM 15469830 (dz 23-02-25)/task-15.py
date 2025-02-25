def f(A):
    for x in range(90, 101):
        f = not(x & 79 == 0) and ((x & 31 == 0) <= (not(x & A == 0)))
        if not f:
            return False
    return True

ans = []
for A in range(0, 1000):
    if f(A):
        ans.append(A)
print(min(ans))

# otvet:32