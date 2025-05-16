def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for n in range(2, 10000):
    r = convert(n, 2)
    odin = r[1::2].count('1')
    null = r[::2].count('0')
    r = abs(odin - null)
    if r == 5:
        print(n)
        break

# otvet: 1023