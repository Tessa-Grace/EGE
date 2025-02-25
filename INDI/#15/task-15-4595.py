# 4595

def f(A):
    for x in range(1, 1000):
        f = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)
        if not f:
            return False
    return True

ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(min(ans))

# otvet: 74