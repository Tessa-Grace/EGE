from itertools import product

alph = '0123456789ABCDEF'

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != 0 and val.count('6') == 2:
        val = val.replace('0', '*').replace('2', '*')
        val = val.replace('4', '*').replace('8', '*')
        val = val.replace('A', '*').replace('C', '*')
        val = val.replace('E', '*')
        if '*6' not in val and '6*' not in val and '66' not in val:
            count += 1
print(count)

# otvet: 4416 ОШИБКА