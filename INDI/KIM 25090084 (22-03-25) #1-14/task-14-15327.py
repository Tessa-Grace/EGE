from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
num = convert(num, 27)

count = 0
for i in num:
    if i in printable[10:]:
        count += 1

print(count)

# otvet: 3368