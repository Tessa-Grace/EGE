from idlelib.debugger_r import GUIAdapter
from itertools import permutations

graph = 'AG GF FE ED DA AB BC CD GB'.split()
matrix = '26 147 456 236 37 134 25'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C D G A F B E
# P = AB + BG + GA = 12 + 13 + 17 = 42
# otvet: 42


