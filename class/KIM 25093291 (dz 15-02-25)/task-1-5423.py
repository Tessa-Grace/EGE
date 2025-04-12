from itertools import permutations

graph = 'АБ БД ДЕ ЕЗ ЗЖ ЖВ ВГ ГД АД ВЗ'.split()
matrix = '245 15 478 135 1246 58 38 367'.split()

print(*range(1, 9))
for i in permutations('АБДЕЗЖВГ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# А Б З Е Д Г Ж В
# А Б В Г Д Е Ж З
# Б А З Е Д Г Ж В
# Б А В Г Д Е Ж З

# 1-АБ 2-АБ 3-ВЗ 4-ЕГ 5-Д 6-ЕГ 7-Ж 8-ВЗ
# ГАБДЕЗ (412568) = 5+1+2+1+2 = 11
# otvet: 11