from itertools import product

alph = sorted('ПРАВД')

ans = []
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if val.count('А') == 0 and val.count('П') == 1 and \
            val.count('Р') == 1 and val.count('В') == 1 and \
            val.count('Д') == 1:
        ans.append(pos)
print(ans[0])

# otvet 195