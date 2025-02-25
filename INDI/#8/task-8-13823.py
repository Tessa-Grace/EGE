#13823

from itertools import product

alph = sorted('МИЗАНТРОП')

ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'Н' and val.count('Р') == 2:
        ans.append(pos)
print(ans[-1])

#otvet: 32712