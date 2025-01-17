from itertools import product

alph = '012345678'
nechet = '1357'

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val[0] not in nechet and \
            val[-1] != '1' and val[-1] != '8'\
        and val.count('3') <= 1:
        count += 1
print(count)

# otvet: 18944