from itertools import permutations

graph = 'AE EH HG GC CF FA ED DF DB BH BG'.split()
matrix = '367 568 18 58 247 127 156 234'.split()

print(*range(1, 9))
for i in permutations('AEHGCFDB'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# G D C A E B H F
# CG=19 + HE=27 = 46
# otvet: 46