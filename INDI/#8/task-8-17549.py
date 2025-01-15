from itertools import product

alph = sorted('ФОКУС')

ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if 'Ф' not in val and val.count('У') == 2:
        ans.append(pos)

print(ans[-1])

# otvet: 2313