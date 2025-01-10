from string import digits, ascii_uppercase
alph = digits + ascii_uppercase

for x in alph[:26]:
    num1 = int('27' + x + '98876', 26)
    num2 = int('26' + x + '51', 26)
    num3 = int('15' + x + '47', 26)
    num4 = int('62' + x + '5', 26)
    num = num1 + num2 + num3 + num4
    if num % 25 == 0:
        print(num // 25)
        break

# otvet: 739259957