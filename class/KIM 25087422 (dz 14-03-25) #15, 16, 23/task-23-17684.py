def f(current, final):
    if current == final:
        return 1
    if current < final:
        return 0
    return f(current - 2, final) + f(current // 2, final)
print(f(38, 10) * f(10, 2))

# otvet: 30