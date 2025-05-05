from itertools import product, repeat

alph = '012345678'
nechet = '1357'

count = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val[0] not in nechet and \
        int(val[-1]) % 3 != 0 and val.count('6') >= 1:
        count += 1

print(count)

# otvet: 827352