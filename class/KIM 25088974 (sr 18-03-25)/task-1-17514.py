from itertools import *

graph = 'AB BH HF FD DC CE EA AH GE GF GC'.split()
matrix= '247 148 578 126 38 47 136 235'.split()

print(*range(1, 9))
for i in permutations('ABHFDCEG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7 8
# G E H C B D F A

# BH=30 + AE=8 = 38

#otvet: 38