from itertools import permutations

graph = 'AE EC CG GF FB BD DA FD GE'.split()
matrix = '234 136 12 157 467 25 45'.split()

print(*range(1, 8))
for i in permutations('AECGFBD'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# G E C F D A B
# F D B G E A C

# B=3 C=7
# otvet: 37