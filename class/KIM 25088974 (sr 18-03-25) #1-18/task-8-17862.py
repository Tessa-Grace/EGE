from itertools import *

count = 0
for val in product('0123456789AB', repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 1:
        val = val.replace('9', '*').replace('A', '*').replace('B', '*')
        if val.count('*') <= 3:
            count += 1
print(count)

# otvet: 67476