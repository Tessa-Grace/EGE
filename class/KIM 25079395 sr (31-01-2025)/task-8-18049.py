from itertools import product

alph = '012345678'

count = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val[0] != '2' and val[0] != '4' and val[0] != '6':
        if val[-3] != val[-2] and val[-2] != val[-1] and val[-3] != val[-1]:
            count += 1
print(count)

# otvet: 1837080