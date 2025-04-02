def f(x, y, s):
    if x + y >= 127: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 2, y,  s - 1), f(x * 3, y, s - 1),
         f(x, y + 2,  s - 1), f(x, y * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 123) if f(2, s,  2)])
print('20)', [s for s in range(1, 123) if f(2, s, 3) and not f(2, s, 1)])
print('21)', [s for s in range(1, 123) if f(2, s, 4) and not f(2, s, 2)])

# otvet:
# 19) [41]
# 20) [39, 40]
# 21) [38]