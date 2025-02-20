#17798

from itertools import product

alph = sorted('МИНУС')
gl = 'ИУ'
sogl = 'МНС'

ans = []
for pos, val in enumerate(product(alph,repeat=4), start=1):
    val = ''.join(val)
    
    c_gl = 0
    c_sogl = 0
    for i in val:
        if i in gl:
            c_gl += 1
        else:
            c_sogl += 1
    if sogl >= gl:
        ans.append(pos)
print(ans[-1])

#Otvet: 625