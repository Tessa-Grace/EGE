from itertools import permutations

graph = 'AB BD DF FG GE EC CA BC DE'.split()
matrix = '67 567 457 35 234 12 123'.split()

print(* range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7
# F E B A C G D
# G D C A B F E
# D=2 E=7 в порядке НЕВОЗРАСТАНИЯ
# otvet: 72
