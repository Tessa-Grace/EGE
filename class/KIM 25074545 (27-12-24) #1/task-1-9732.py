from itertools import permutations

graph = 'CG GA AD BD BF FC BE FE CE EG'.split()
matrix = '47 357 2567 16 236 345 123'.split()

print(*range(1, 8))
for i in permutations('CGADBFE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# C=2 F=5
# otvet: 25

