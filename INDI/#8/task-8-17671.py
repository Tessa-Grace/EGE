from itertools import product

alph = sorted('ЛАЙМ')

ans = []
for pos, val in enumerate(product(alph, repeat=5),start=1):
    val = ''.join(val)
    if val not in 'М' and val not in 'Л' and 'ЙЙ' not in val:
        ans.append(pos)
print(ans[-1])

#Otvet: 1024