from itertools import permutations

graph = 'AV VE EJ JD DG GB BV VG GJ GE'.split()
matrix = '24567 146 5 12 1367 125 15'.split()

print(*range(1, 8))
for i in permutations('AVEJDBG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7
# G J A D V E B
# EJ=25
# otvet: 25