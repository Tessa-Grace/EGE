from itertools import product

alph = sorted('МИНУС')

ans = []
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if (val.count('М') + val.count('Н') + val.count('С')) >= val.count('У') + val.count('И'):
        ans.append(pos)
print(ans[-1])

# otvet: 619