from itertools import *

graph = 'AG GF FB BD DE EA CG CB CE'.split()
matrix = '47 57 45 136 236 457 126'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# A D F G B C E
# A F D E B C G
# D A F B G C E
# D F A E G C B
# F A D B E C G
# F D A G E C B

# C-6  B-4/5/7 G-4/5/7 E-4/5/7 => 11+13+17 = 41
# otvet: 41