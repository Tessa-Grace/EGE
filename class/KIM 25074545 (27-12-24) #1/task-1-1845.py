from itertools import permutations

graph = 'AB BG AV BV VD DZ GD GE EZ'.split()
matrix = '67 467 456 35 234 123 12'.split()

print(*range(1, 8))
for i in permutations('ABVGDEZ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
