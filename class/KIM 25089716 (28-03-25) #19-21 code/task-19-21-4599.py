def f(x, y, s): #x- изначально камней , y - кол-во камней во второй куче, s- кол-во шагов
    if x + y >= 259: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1), f(x, y + 1, s - 1),
         f(x * 2, y, s - 1), f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 242) if f(17, s, 2)])
print('20)', [s for s in range(1, 242) if f(17, s, 3) and not f(17, s, 1)])
print('21)', [s for s in range(1, 242) if f(17, s, 4) and not f(17, s, 2)])

# otvet:
# 19) 61 -> удалив (if (s - 1) % 2 == 0 else all(h)), чтобы получить ответы
# 20) [112, 120]
# 21) [111, 119]
