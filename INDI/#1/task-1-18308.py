from itertools import permutations

graph = 'AK KC CD DH HG GF FE ED DB BK DG'.split()
matrix = '45 489 45 12379 136 5 48 27 24'.split()

print(*range(1, 10))
for i in permutations('AKBCEDHFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7 8 9
# B G C D K A E F H
# C G B D K A E F H
# FE=8 + ED=15 = 23
# otvet: 23