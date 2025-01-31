def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num = 343**1515 - 6 * 49**1520 + 5 * 49**1510 - 3 * 7**1530 - 1550
print(convert(num, 7).count('0'))

# otvet: 19
