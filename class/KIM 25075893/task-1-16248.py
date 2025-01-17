from itertools import permutations

graph = 'BA AD DF FG GE EC CB AC ED EF'.split()
matrix = '347 3456 1245 1237 236 25 14'.split()

print(*range(1, 8))
for i in permutations('BACDFGE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7
# A E D C F G B
# F C D E A B G

# E=2 C=4
# otevt: 24