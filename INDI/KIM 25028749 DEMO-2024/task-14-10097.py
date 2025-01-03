num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
res = ''
while num:
    res += str(num % 25)
    num //= 25
res = res[::-1]
print(res.count('0'))

# otvet: 9