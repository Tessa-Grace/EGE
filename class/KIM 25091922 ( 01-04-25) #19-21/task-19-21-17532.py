def f(x, y, s):
    if x + y >= 65: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1),
         f(x * 3, y, s - 1),
         f(x, y + 1, s - 1),
         f(x, y * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h) # если в 19) первый ход неудачный, то all меняем на any, а потом надо вернуть обратно

print('19)', [s for s in range(1, 59) if f(6, s, 2)])
print('20)', [s for s in range(1, 59) if f(6, s, 3) and not f(6, s, 1)])
print('21)', [s for s in range(1, 59) if f(6, s, 4) and not f(6, s, 2)])

# otvet:
# 19) 7
# 20) 10, 19
# 21) 18