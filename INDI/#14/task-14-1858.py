def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num = 4 * 625**9 - 25**15 + 2 * 5**11 - 7
print(convert(num, 5).count('4'))

# otvet: 15
