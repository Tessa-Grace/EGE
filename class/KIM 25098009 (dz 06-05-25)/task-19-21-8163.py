def f(x, s):
    if x >= 348: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 2, s - 1),
         f(x + 4, s - 1),
         f(x * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else any(h)

print('19)', [s for s in range(1, 347) if f(s, 2)])
print('20)', [s for s in range(1, 347) if f(s, 3) and not f(s, 2)])
print('21)', [s for s in range(1, 347) if f(s, 4) and not f(s, 3)])

# otvet:
# 19) [39]
# 20) [38, 110]
# 21) [108]