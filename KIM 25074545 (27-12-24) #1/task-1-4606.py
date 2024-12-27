from itertools import permutations

graph = 'CE CA CD DH HE EG GF FB FA AB'.split()
matrix = '68 47 45 237 368 15 248 157'.split()
print(*range(1, 9))
for i in permutations('CDHEGFBA'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 13 + 5 = 18
# otvet: 18