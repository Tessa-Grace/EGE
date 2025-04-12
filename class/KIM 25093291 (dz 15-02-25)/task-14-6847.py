ans = []
for x in range(1, 111):
    num1 = x*111**3 + 3*111**2 + 2*111 + 1
    num2 = 1*211**3 + 7*211**2 + x*211 + 4
    num = num1 + num2
    if num % 111 == 0:
        ans.append(num // 111)
print(max(ans))

# otvet: 297262