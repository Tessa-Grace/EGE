from itertools import permutations

graph = 'АБ БД ДЖ ЖЗ ЗЕ ЕГ ГВ ВА ВБ ГД ЕЖ'.split()
matrix = '356 368 128 67 127 147 456 23'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# Г Б В З Д Е Ж А
# Д Е Ж А Г Б В З

# кратчайший путь = АВГЕЗ=5+1+2+2=10
# otvet: 10