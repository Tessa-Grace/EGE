from itertools import permutations

graph = 'АВ ВБ ВГ ГЖ ГЕ ЕД'.split()
matrix = '6 356 2 5 247 12 5'.split()

print(*range(1, 8))
for i in permutations('АВБГЖЕД'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6
# Д Г Ж А В Е Б
# Д Г Ж Б В Е А

# ГЖ = 7
# otvet: 7