def f(cur, fin, count = 0):
    if cur == fin:
        return 1
    if cur > fin:
        return 0
    if count == 0 and cur < 23:
        return f(cur + 2, fin, count=1) + f(cur * 2, fin, count=1)
    return f(cur + 2, fin, count) + f(cur * 2, fin, count) + f(cur + 5, fin, count)

print(f(7, 23) * f(23, 35))

# otvet: 44