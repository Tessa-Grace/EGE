from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

num = 2*729**2014 + 2*243**2016 - 2*81**2018 + 2*27**2020 - 2*9**2022 - 2024
num = convert(num, 27)
count = 0
for i in str(num):
    if i in alph[10:27]:
        count += 1

print(count)

# otvet: 2687
