from itertools import permutations

graph = 'AB BC CF FG GE EA DA DB DC DF DE'.split()
matrix = '2356 145 146 23 127 137 156'.split()

print(*range(1, 8))
for i in permutations('ABCFGED'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7
# D F E G C A B
# D E F G A C B
# A=5 C=6
# otvet: 65