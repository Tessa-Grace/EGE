# 1865

def f(current, final):
    if current == final:
        return 1
    if current > final or current == 12: # исключаем число 12 из траектории вычислений, как указано в условии к задаче
        return 0

    return f(current + 1, final) + f(current + 2, final) + f(current * 3, final)

print(f(2, 9) * f(9, 12))

#otvet: 75