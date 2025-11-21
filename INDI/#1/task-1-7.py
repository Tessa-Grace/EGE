from itertools import permutations

graph = 'АГ ГБ БД ДВ ВИ ИЖ ЖЕ ЕА ГЖ БЖ ЖД'.split()
matrix = '256 14568 45 23 123 127 68 27'.split()

print(*range(1, 9))
for i in permutations('АГБДВИЖЕ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# Б Ж А Е Г Д В И -
# Б Ж В И Д Г А Е +

# ВИ = 15
# otvet: 15