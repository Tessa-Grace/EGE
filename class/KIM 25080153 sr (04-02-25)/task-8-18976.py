from itertools import product
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
alph = alph[:20]
chet = alph[::2]
nechet = alph[1::2]

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and int(val[0], 20) + int(val[-1], 20) == 26:
        for i in val:
            if i in chet:
                val = val.replace(i,'*')
            if i in nechet:
                val = val.replace(i, '!')
        if val == '*!*!*' or val == '!*!*!':
            count += 1
print(count)

# otvet: 13000
