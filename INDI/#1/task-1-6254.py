from itertools import permutations

graph = 'AE ED DB BF FG GA CB CE CG'.split()
matrix = '47 57 45 136 236 457 126'.split()

print(*range(1, 8))
for i in permutations('AEDBFGC'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 1 2 3 4 5 6 7
# A D F G B C E
# A F D E B C G
# D A F B G C E
# D F A E G C B
# F A D B E C G
# F D A G E C B
# 1-ADF
# 2-ADF
# 3-ADF
# 4-EBG
# 5-EBG
# 6-C
# 7-EBG
# ____???______BDE=42
# 435=60
# 527=29+19=48
# 714=41+37=78
# 725=19+23=42
# otvet: 42