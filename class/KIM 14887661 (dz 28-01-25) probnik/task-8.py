from itertools import *

alph = '0123456789AB'

count = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val.count('B') == 2:
        val = val.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*').replace('8', '*').replace('A', '*')
        val = val.replace('1', '!').replace('3', '!').replace('5', '!').replace('7', '!').replace('9', '!').replace('B', '!')
        if val == '*!*!*!*' or val == '!*!*!*!':
            count += 1
print(count)

# otvet: 51840