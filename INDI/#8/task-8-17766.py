#17766

from itertools import product

alph = sorted('СЕНТЯБРЬ')

ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'Р' and val not in 'Ь':
        ans.append(pos)
print(ans[-1])

#Otvet: 16384