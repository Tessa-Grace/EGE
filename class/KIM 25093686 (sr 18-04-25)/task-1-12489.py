from itertools import permutations

graph = 'АБ БГ ГЕ ЕЗ ЗЖ ЖД ДГ ГВ ВА АГ ГЗ ГЖ'.split()
matrix = '235 13 1245678 36 13 347 368 37'.split()

print(*range(1, 9))
for i in permutations('АБГЕЗЖДВ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# otvet:
# 1 2 3 4 5 6 7 8
# А Б Г Е В З Ж Д
# А Б Г Д В Ж З Е
# А В Г Е Б З Ж Д
# А В Г Д Б Ж З Е

#г-3, з-6, ж-7
#gz=16+zj=17+jg=11=44
# otvet: 44

