from itertools import *

alph = '012345678'
lt = []
count = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val[-1] not in '347' and \
            '000' not in val and '111' not in val and '222' not in val and \
            '333' not in val and '444' not in val and '555' not in val and \
            '666' not in val and '777' not in val and '888' not in val:
        count += 1
print(count)

# otvet: 2676053