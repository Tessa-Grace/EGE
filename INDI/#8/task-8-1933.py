from itertools import *

alph = 'КЛАБХАУС'

count = 0
for val in set(permutations(alph, r=8)):
    val = ''.join(val)
    if val[0] != val[1] != val[2] != val[3] != val[4] != val[5] != val[6] != val[7]:
        count += 1
print(count)

# otvet: 15120