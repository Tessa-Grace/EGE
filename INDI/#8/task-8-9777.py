from itertools import product

alph = sorted('КОМПЬЮТЕР')

ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'Ь' and val.count('К') == 2 and pos % 2 != 0:
        ans.append(pos)

print(ans[-1])

#Otvet: 58979
