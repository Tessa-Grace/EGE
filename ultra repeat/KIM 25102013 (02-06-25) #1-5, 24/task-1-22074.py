from itertools import permutations

graph = 'АБ БВ ВД ДЖ ЖА ГБ ГЕ ЕЖ ЕВ'.split()
matrix = '347 456 156 12 23 237 16'.split()

print(*range(1, 8))
for i in permutations('АБВДЖГЕ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# Б Ж В А Д Е Г
# Ж Б Е А Г В Д

# БГ=11 + ЖД=31 =42
# otvet: 42