from itertools import permutations

graph = 'AC CB BD DE EF FG GA CD CE CF CG'.split()
matrix = '234567 17 157 156 134 14 123'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C A F D E B G
# C B E G F A D
# E-? F-?

# otvet: 35