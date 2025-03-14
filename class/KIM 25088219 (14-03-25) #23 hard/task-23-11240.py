def f(current, final, B=False):
    if current == final:
        return 1
    if current > final + 1:
        return 0
    if B:
        return f(current +2, final) + f(current * 3, final)
    return f(current + 2, final) + f(current ** 2, final, True) + f(current * 3, final)

print(f(2, 64))

# otvet: 55