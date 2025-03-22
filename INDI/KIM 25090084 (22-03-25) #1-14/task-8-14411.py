from itertools import product

alph = sorted(set('СУБЛИМАЦИЯ'))

ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[-1] != 'Я' and \
            (val.count('У') + val.count('И') + val.count('А') + val.count('Я') == 2):
        ans.append(pos)
print(ans[-1])

# otvet: 58955
