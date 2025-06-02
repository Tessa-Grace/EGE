from itertools import permutations

graph = 'AB BG GE EF FA DA DF DC CE CB'.split()
matrix = '457 567 45 136 123 247 126'.split()

print(*range(1, 8))
for i in permutations('ABGEFDC'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C A G E B F D
# C F G B E A D

# AB=18 + EF=4 = 22
# otvet: 22