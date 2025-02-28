from itertools import *

graph = 'AB BC CD DE EH HA GA GH GF FE FC'.split()
matrix = '568 36 247 368 178 124 35 145'.split()

print(*range(1, 9))
for i in permutations('ABCDEHGF'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# H D C F A E B G
# otvet: 64815