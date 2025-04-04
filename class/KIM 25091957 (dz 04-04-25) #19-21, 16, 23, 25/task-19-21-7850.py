def f(x, s):
    if x >= 73: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, s - 1),
         f(x + 3, s - 1),
         f(x * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 73) if f(s, 2)])
print('20)', [s for s in range(1, 73) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 73) if f(s, 4) and not f(s, 2)])

# otvet:
# 19) [36]
# 20) [18, 33]
# 21) [32, 34]