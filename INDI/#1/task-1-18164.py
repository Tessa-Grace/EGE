from itertools import permutations

graph = 'AB BD DF FE EC CA DG FG CG'.split()
matrix = '457 46 567 12 136 235 13'.split()

print(*range(1, 8))
for i in permutations('ABDFECG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C B F A G D E
# A=4 G=5
# otvet: 54