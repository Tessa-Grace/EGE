from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
num = convert(num, 25)
print(num.count('0'))

# otvet: 18
