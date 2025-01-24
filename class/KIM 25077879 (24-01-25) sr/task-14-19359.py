from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:22]:
    num1 = 'A23'+ x + 'AC0'
    num2 = 'GB' + x + '21670'
    num = int(num1, 22) + int(num2, 22)
    if num % 21 == 0:
        ans.append(num // 22)
print(max(ans))

# otvet: 1923296823