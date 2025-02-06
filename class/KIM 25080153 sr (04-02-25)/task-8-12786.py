from itertools import *

count = 0
for val in set(permutations('МАКАКА', 6)):
    val = ''.join(val)
    if 'АА' not in val and 'КК' not in val:
        count += 1
print(count)

# otvet: 10