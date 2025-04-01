def f(x, y, s):
    if x + y >= 44: return s % 2 == 0
    if s == 0: return False
    h = [f(x + y, y, s - 1),
         f(x, x + y, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(0, 100) if f(11, s, 1)]) # правая граница в range выбирается, когда появляются в списке
print('20)', [s for s in range(0, 20) if f(11, s, 2)])

ans = []
for s1 in range(0, 30):
    for s2 in range(0, 30):
        if f(s1, s2, 3):
            ans.append([abs(s2 - s1), s1, s2])

print('21)', min(ans))

# otvet:
# 19) [17]
# 20) [8]
# 21) [7, 7]
