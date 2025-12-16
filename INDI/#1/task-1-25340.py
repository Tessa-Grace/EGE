from itertools import permutations

graph = 'AC CB BH HD DA HF FE EG GC GA'.split()
matrix = '368 34 126 27 67 135 458 17'.split()

print(*range(1, 9))
for i in permutations('ACBHDFEG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7 8
# A E G F B C H D
# C E G F D A H B

# GE=15 + FH=13 =28
# otvet: 28
