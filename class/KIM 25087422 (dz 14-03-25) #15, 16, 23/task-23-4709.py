def f(current, final):
    if current == final:
        return 1
    if current > final or current == 17:
        return 0
    return f(current + 1, final) + f(current * 2, final)
print(f(1, 10) * f(10, 35))

# otvet: 98