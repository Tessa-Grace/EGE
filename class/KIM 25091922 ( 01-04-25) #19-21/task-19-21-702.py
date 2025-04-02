def f(x, s):
    if 36 <= x <= 85: return s % 2 == 0
    if x > 85: return s % 2 != 0
    if s == 0: return False
    h = [f(x + 2, s - 1),
         f(x * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19_1)', f(30, 101)) # берем нечет по максимуму,чтобы рассмотреть все возможные варианты победы Пети
# otvet: True => Петя
print('19_2)', f(32, 100)) # берем чет по максимуму,чтобы рассмотреть все возможные варианты победы Вани
# otvet: True => Ваня

print('20_1)', f(8, 100))
# otvet: False => Петя
print('20_2)', f(10, 100))
# otvet: False => Ваня

print('21)', f(6, 100))
# otvet: False => Ваня