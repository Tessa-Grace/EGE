from itertools import product

alph = sorted('АРГУМЕНТ')

ans = []
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if val.count('А') <= 1 and val.count('Р') <= 1 and val.count('Г') <= 1 and val.count('У') <= 1 \
            and val.count('М') <= 1 and val.count('Е') <= 1 and val.count('Н') <= 1 and val.count('Т') <= 1:
        if list(val) == sorted(val):
            ans.append(pos)
print(ans[-1])

# otvet: 2424