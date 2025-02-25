from itertools import permutations

graph = 'AD DE EA VG GB BV VA VE GA GD BD BE'.split()
matrix = '2456 1346 2456 1235 1346 1235'.split()

print(*range(1, 7))

for i in permutations('ADEVGB'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y, in graph):
        print(*i)

# 1 2 3 4 5 6
# A D B E V G

# adb-123-
# aeb-143-
# avb-153-
# agb-163-5+7=12
# ОШИБКА!