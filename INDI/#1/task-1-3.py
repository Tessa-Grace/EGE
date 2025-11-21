from itertools import permutations

graph = 'АБ БВ ВГ ГК КЕ ЕД ДА АВ ДВ ВЕ ЕГ'.split()
matrix = '357 34 12467 236 17 347 1356'.split()

print(*range(1, 8))
for i in permutations('АБВГКЕД'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6
# Г Б В А К Д Е
# АД = 46
# otvet: 46