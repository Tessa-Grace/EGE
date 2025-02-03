# 19406
from string import digits, ascii_uppercase
alph = digits + ascii_uppercase

ans = []
for x in alph[1:35]:
    num1 = int('6'+ x + 'QR' + x, 35)
    num2 = int(f'{x}59sh', 35)
    num3 = int('PH' + x + '69YW', 35)
    num = num1 + num2 + num3
    moda_variants = []
    for i in '0123456789':
        moda_variants.append([str(num).count(i),int(i)])
    moda = max(moda_variants)
    if num % moda[1]**2 == 0:
        print(num // moda[1]**2)

# otvet: 46926015711