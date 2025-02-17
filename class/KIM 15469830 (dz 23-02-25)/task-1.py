from itertools import *

graph = 'AB BG GE EZ ZJ JD DG GV VA GA GZ GJ'.split()
matrix = '235 13 1245678 36 13 347 368 37'.split()

print(*range(1, 9))
for i in permutations('ABGEZJDV'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# A B G E V Z J D
# A B G D V J Z E
# A V G E B Z J D
# A V G D B J Z E

# G=П3 Z=П6 J=П7
# GZ=16 ZJ=17 JG=11
# P = 16 + 17 + 11 = 44

# otvet: 44
