from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

num = 3*3125**9 + 2*625**8 - 4*625**7 + 3*125**6 - 2*25**5 - 2024
num = convert(num, 25)
print(num.count('0'))

# otvet: 9