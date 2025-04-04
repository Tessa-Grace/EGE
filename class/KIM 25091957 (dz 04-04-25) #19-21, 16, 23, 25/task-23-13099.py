def f(cur, fin, A=False):
    if cur == fin: return 1
    if cur > fin + 1: return 0
    if A: return f(cur * 2, fin) + f(cur * 3, fin)
    return f(cur - 1, fin, True) + f(cur * 2, fin) + f(cur * 3, fin)

print(f(3, 15))

# otvet: 6