from itertools import product

alph = '01234567'

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('6') == 1 and val[0] != '0':
        val = val.replace('1', '*').replace('3', '*')
        val = val.replace('5', '*').replace('7', '*')
        if '*6' not in val and '6*' not in val:
            count += 1
print(count)

# otvet: 2961