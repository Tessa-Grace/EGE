from itertools import *

graph = 'AV VG GD DB BJ JA AZ JD ZV ZG ZD'.split()
matrix = '256 135 2457 37 1236 157 346'.split()

print(*range(1, 8))
for i in permutations('AVGDBJZ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7
# V G D B Z A J
# otvet: VGDBZAJ
