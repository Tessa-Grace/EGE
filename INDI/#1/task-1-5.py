from itertools import permutations

graph = 'ДГ ГВ ВА АБ БЕ ЕЖ ЖД ДЕ ДБ ДА ДВ'.split()
matrix = '457 567 45 135 123467 25 125'.split()

print(*range(1, 8))
for i in permutations('ДГВАБЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6
# А Е Г В Д Ж Б
# Б В Ж Е Д Г А

# АБ = 17
# otvet: 17