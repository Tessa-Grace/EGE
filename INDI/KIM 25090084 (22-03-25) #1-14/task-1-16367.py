from itertools import *

graph = 'AG GB BE EF FD DC CA AB FC'.split()
matrix = '246 16 57 15 347 127 356'.split()

print(*range(1, 8))
for i in permutations('AGBEFDC'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# B G D E F A C
# F D G E B C A

# G=2 D=3
# otvet: 23