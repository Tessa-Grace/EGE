from itertools import permutations

graph = 'АГ ГД ДЖ ЖЕ ЕВ ВБ БА АВ ДЕ'.split()
matrix = '67 346 24 235 47 127 156'.split()

print(*range(1, 8))
for i in permutations('АГДЖЕВБ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# Ж В Б А Г Е Д
# Б Е Ж Д Г В А
# ВЕ=26
# otvet: 26