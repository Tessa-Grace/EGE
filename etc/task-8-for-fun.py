from itertools import product
from string import ascii_uppercase

alph = sorted('QWERTYUIOASDFGHJKLZXCVBNM')

count = 0
for r in range(1, 7):
    for val in product(ascii_uppercase, repeat=r):
        val = ''.join(val)
        count += 1
        if val == 'FEDABC':
            print(count)

# otvet: 73644171