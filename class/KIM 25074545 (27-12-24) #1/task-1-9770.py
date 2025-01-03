from itertools import permutations

graph = 'CA CB CF FD DH HG GA AB BE ED'.split()
matrix = '56 378 26 68 17 134 258 247'.split()

print(*range(1, 9))
for i in permutations('ACFDHGBE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# BC= 18  GH= 43
# 18 + 43 = 61
# otvet: 61

