def s_rectangle(a, b):
    s = (a + b) * 2
    return s

def f(A):
    for x in range(1, 10000):
        for y in range(1, 10000):
            f = (not(s_rectangle(x, y) > (A + 13))) <= ((s_rectangle(28, y) > 520) or (s_rectangle(x, 25) > 800))
            if not f:
                return False
        return True

ans = []
for A in range(-10000, 10000):
    if f(A):
        ans.append(A)

print(max(ans))

# otvet : -10