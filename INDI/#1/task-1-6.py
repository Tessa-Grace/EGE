from itertools import permutations

graph = 'AE EG GF FB BA AC CE CD DB DF'.split()
matrix = '235 146 145 236 137 247 56'.split()

print(*range(1, 8))
for i in permutations('AEGFBDC'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# A B C D E F G -
# B A D C F E G -
# D C B A F E G +
# C D A B E F G  +

# AB = 34
# otvet: 34