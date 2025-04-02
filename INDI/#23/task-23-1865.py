def f(current, final):
    if current == final:
        return 1
    if current > final or current == 12: # если действия на возрастание, то >, если на убывание (- /), то <
        return 0

    return f(current + 1, final) + f(current + 2, final) + f(current * 3, final)

print(f(2, 9) * f(9, 12))

#otvet: 75