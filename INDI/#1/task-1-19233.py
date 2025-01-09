from itertools import permutations

graph = 'AF FH HC CB BD DG GA GF EB ED EH'.split()
matrix = '234 157 147 138 268 58 23 456'.split()

print(*range(1, 9))
for i in permutations('AFHCBDGE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7 8
# E H B D F A C G
# AG=4 + DE=7 = 11
# otvet: 11