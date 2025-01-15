from itertools import product

alph = sorted('КОДИМ')

ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('М') == 2 and 'ММ' not in val:
        ans.append(pos)

print(ans[-1])

# Otvet: 3099