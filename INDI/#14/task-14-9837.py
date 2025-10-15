# from string import digits, ascii_uppercase
#
# alph = digits + ascii_uppercase
#
# ans = []
# for x in alph[:23]:
#     num1 = int('7' + x + '38596', 23)
#     num2 = int('14' + x + '36', 23)
#     num3 = int('61' + x + '7', 23)
#     num = num1 + num2 + num3
#     if num % 22 == 0:
#         ans.append(num // 22)
# print(min(ans))
#
# # otvet:

from string import *

ans = []
alph = digits + ascii_uppercase

for x in alph[:27]:
    n1 = int('2107' + x + '792', 27)
    n2 = int('565'+ x +'211', 27)
    num = n1+n2
    if num % 26 == 0:
        ans.append(num // 26)
print(min(ans))

# otvet: 897607140