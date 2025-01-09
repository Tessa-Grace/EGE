# 17627

from itertools import product
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

count = 0
for val in product(alph[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and \
            sum(i in ascii_uppercase[:5] for i in val) >= 2:
        count += 1
print(count)

# otvet: 83175