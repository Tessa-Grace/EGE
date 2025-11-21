from itertools import permutations

graph = 'АБ БВ ВГ ГД ДМ МК КА КИ МИ ИБ ИГ БЕ ЕГ ЕВ'.split()
matrix = '468 3689 279 158 47 12 3589 1247 237'.split()

print(*range(1, 10))
for i in permutations('АБВГДМКИЕ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8 9
# М Г В К А Д Б И Е -
# М Г Е К А Д Б И В -
# К Б В М Д А Г И Е +
# К Б Е М Д А Г И В -

# МД = 41
# otvet: 41