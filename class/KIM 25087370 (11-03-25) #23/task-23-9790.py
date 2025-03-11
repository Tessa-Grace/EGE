def f(current, final):
    if current == final:
        return 1
    if current < final or current == 9 or current == 16:
        return 0
    return f(current - 1, final) + f(current - 2, final) + f(current // 3, final)
print(f(19, 3))

# otvet: 180