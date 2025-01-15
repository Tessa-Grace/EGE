from itertools import product

alph = '01234567'

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1 and \
            '16' not in val and '61' not in val and \
            '36' not in val and '63' not in val and \
            '56' not in val and '65' not in val:
        count += 1
print(count)

#otvet: 4480 ОШИБКА!