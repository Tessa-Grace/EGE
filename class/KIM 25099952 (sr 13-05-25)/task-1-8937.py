from itertools import permutations

graph = 'АБ БД ДГ ГЖ ЖЗ ЗЕ ЕВ ВА БВ ДЕ ЖД ЖЕ'.split()
matrix = '3578 346 1258 26 13 248 18 1367'.split()

print(*range(1, 9))
for i in permutations('АБДГЖЗЕВ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7 8
# Ж Б Д А Г В З Е
# Ж В Е А З Б Г Д

# д=3 е=8
# otvet: 15