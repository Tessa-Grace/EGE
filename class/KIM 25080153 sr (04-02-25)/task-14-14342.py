from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for p in range(36, 1, -1):
    num1  = int('CNG', p)
    num2 = int('BO', p)
    num3 = int('OM', p)
    num4 = int('BL4', p)
    if num1 == num2 + num3 + num4:
        print(p)

#otvet: 34

