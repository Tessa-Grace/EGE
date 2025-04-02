def f(current, final):
    if current == final:
        return 1
    if current < final or current == 7:
        return 0
    return f(current - 1, final) + f(current - 3, final) + f(current // 2, final)
print(f(19, 10) * f(10, 3))

# otvet: 133