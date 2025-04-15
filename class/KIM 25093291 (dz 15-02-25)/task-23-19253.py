def f(cur, fin):
    if cur == fin: return True
    if cur < fin or cur == 24: return False
    return f(cur - 1, fin) + f(cur - 6, fin) + f(cur // 2, fin)

print(f(34, 29) * f(29, 19) * f(19, 6))

# otvet: 115