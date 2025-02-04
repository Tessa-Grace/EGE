from itertools import product
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

count = 0
for val in product(alph[:20], repeat=5):
    val = ''.join(val)
    for i in val:
        if i in '02468ACEGI':
            val1 = val.replace(i,'*')
        if i in '13579BDFHJ':
            val1 = val.replace(i, '!')
    if (val1 == '*!*!*' or val1 == '!*!*!') and int(val[0]) + int(val[-1] == 26):
        print(val)
        count += 1
print(count)
