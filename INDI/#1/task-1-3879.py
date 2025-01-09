from itertools import permutations

graph = 'АБ БВ ВГ ГА ДЕ ЕИ ИК КД АД БЕ ВИ ГК ДИ'.split()
matrix = '568 578 567 678 123 134 2348 1247'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕИК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# А Е В К Б Г И Д
# А К В Е Г Б И Д
# В Е А К Б Г Д И
# В К А Е Г Б Д И
# АБ=10 + БВ=11 + ВГ=9 + ГА=13 = 23+20 = 43
# otvet: 43