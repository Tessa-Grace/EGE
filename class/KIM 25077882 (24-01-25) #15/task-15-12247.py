def f(A):
    for x in range(1, 1000):
        f = (x & A == 0) or (x & 37 != 0) or (x & 12 != 0)
        if not f:
            return False
    return True

ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

#otvet: 45