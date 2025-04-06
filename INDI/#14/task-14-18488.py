from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 1000):
    num = 7**666 + 7**333 + 49**x - 343
    num = convert(num, 7)
    if num.count('6') == 49:
        print(x)
        break

# otvet: 26