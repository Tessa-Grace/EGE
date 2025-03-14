def f(current, final, A=False):
    if current == final:
        return 1
    if current > final + 1:
        return 0
    if A:
        return f(current * 2, final) + f(current * 3, final)
    return f(current - 1, final, True) + f(current * 2, final) + f(current * 3, final)

print(f(3, 15))

# otvet: 6