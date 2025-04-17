from itertools import *

alph = sorted('ДГИАШЭ')

ans = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'ИАЭ' and val[-1] not in 'ДГШ':
        ans += 1
print(ans)