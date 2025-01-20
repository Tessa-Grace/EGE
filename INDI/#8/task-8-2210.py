from itertools import product

alph = sorted('КРОВЬ')

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != 'Ь' and 'ЬО' not in val and 'ОЬ' not in val and \
        val.count('К') == 1 and val.count('Р') == 1 and val.count('О') == 1 and \
            val.count('В') == 1 and val.count('Ь') == 1:
        count += 1
print(count)

# otvet: 54