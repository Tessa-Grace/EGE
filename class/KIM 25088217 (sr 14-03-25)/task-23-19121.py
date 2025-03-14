def f(current, final):
    if current == final:
        return 1
    if current < final:
        return 0
    return f(current - 3, final) + f(current // 3, final)
print(f(35, 8) * f(8, 1))

# otvet: 3