from itertools import *

alph = 'КОБУРА'

count = 0
for val in permutations(alph, 6):
    val = ''.join(val)
    val = val.replace('К', '*').replace('Б', '*').replace('Р', '*')
    val = val.replace('О', '!').replace('У', '!').replace('А', '!')
    if '!*!*!*' in val or '*!*!*!' in val:
        count += 1
print(count)