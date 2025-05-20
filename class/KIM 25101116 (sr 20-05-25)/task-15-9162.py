def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (not(x * y > a + 13)) <= (28 * y > 520 or x * 25 > 800)
            if not f:
                return False
    return True

ans = []
for a in range(-100, 100):
    if f(a):
        ans.append(a)
print(max(ans))

# otvet: -13