def f(cur, fin):
    if cur == fin:
        return 1
    if cur > fin or cur == 8:
        return 0
    return f(cur + 1, fin) + f(cur + 2, fin) + f(cur * 2, fin)
print(f(3, 14) * f(14, 18))

# otvet: 360