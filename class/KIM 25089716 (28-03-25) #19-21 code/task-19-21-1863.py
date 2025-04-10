def f(x, s): #x- изначально камней, s- кол-во шагов
    if x >= 40: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, s - 1), f(x + 4, s - 1), f(x * 2, s - 1)] # h- ходы
    return any(h) if (s - 1) % 2 == 0 else all(h) # если четный шаг, тогда достаточно одного true,
                                                  # если нечетно, тогда все должно быть true

print('19)', [s for s in range(1,40) if f(s, 2)])
print('20)', [s for s in range(1, 40) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 40) if f(s, 4) and not f(s, 2)])

# otvet:
# 19) [19]
# 20) [15, 18]
# 21) [14, 17]

