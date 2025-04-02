def f(current, final):
    if current == final:
        return 1
    if current < final:
        return 0
    return f(current - 1, final) + f(current // 2, final)

print(f(30, 12) * f(12, 1))

# otvet: 376