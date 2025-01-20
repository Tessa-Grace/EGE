from itertools import *

count = 0
for val in set(permutations('СОТОЧКА', 7)):
    val = ''.join(val)
    if 'ОО' in val or 'АА' in val or 'АО' in val or 'ОА' in val:
        count += 1
print(count)

# otvet: 1800
'''
from itertools import *

combs = ['АА', 'ОО', 'ОА', 'АО']

count = 0
for val in set(permutations('СОТОЧКА')):
    val = ''.join(val)
    if any(i in val for i in combs):
        count += 1
print(count)
'''