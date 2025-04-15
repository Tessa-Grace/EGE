def f(cur, fin):
    if cur == fin: return True
    if cur > fin or cur == 21: return False
    return f(cur + 2, fin) + f(cur + 3, fin) + f(cur * 2, fin)

print(f(7, 14) * f(14, 32))

# otvet: 160