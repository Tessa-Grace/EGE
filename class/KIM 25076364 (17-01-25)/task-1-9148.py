from itertools import permutations

graph = 'AG GJ JZ ZD DV VA BV BA BG GD EJ EZ ED'.split()
matrix = '256 1458 478 237 126 158 348 2367'.split()

print(*range(1, 8))
for i in permutations('AGJZDVBE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# A G Z J B V E D
# A G E J B V Z D
# Z D A V E J B G
# Z D B V E J A G
# B G Z J A V E D
# B G E J A V Z D
# E D A V Z J B G
# E D B V Z J A G
# OSHIBKA!!