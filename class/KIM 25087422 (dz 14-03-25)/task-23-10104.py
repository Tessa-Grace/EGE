def f(current, final):
    if current == final:
        return 1
    if current > final or current == 11:
        return 0
    return f(current + 1, final) + f(current * 2, final) + f(current ** 2, final)
print(f(2, 20) )

# otvet: 37