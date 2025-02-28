from itertools import product

alph = 'КОТБУС'

count = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    if 'КОТ' in val and val[0] != 'О' and val[0] != 'У':
        count += 1
print(count)

# otvet: 33516