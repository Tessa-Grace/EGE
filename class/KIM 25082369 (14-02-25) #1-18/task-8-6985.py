from itertools import product

alph = sorted('МАРКСЛ')

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'КС' not in val and 'СК' not in val and \
            (val.count('М') == 3 and val.count('А') <= 1 and val.count('Р') <= 1 and val.count('К') <= 1 and \
             val.count('С') <= 1 and val.count('Л') <= 1) or \
            (val.count('М') == 1 and val.count('А') <= 3 and val.count('Р') <= 1 and val.count('К') <= 1 and \
             val.count('С') <= 1 and val.count('Л') <= 1) or \
            (val.count('М') == 1 and val.count('А') <= 1 and val.count('Р') <= 3 and val.count('К') <= 1 and \
             val.count('С') <= 1 and val.count('Л') <= 1) or \
            (val.count('М') == 1 and val.count('А') <= 1 and val.count('Р') <= 1 and val.count('К') <= 3 and \
             val.count('С') <= 1 and val.count('Л') <= 1) or \
            (val.count('М') == 1 and val.count('А') <= 1 and val.count('Р') <= 1 and val.count('К') <= 1 and \
             val.count('С') <= 3 and val.count('Л') <= 1) or \
            (val.count('М') == 1 and val.count('А') <= 1 and val.count('Р') <= 1 and val.count('К') <= 1 and \
             val.count('С') <= 1 and val.count('Л') <= 3):
            ans.append(pos)
print(ans[-1])

# otvet: 46605


