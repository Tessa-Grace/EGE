from fnmatch import fnmatch

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for i in range(int('12135664', 7) - int('12135664', 7) % 333, 10 ** 9, 333):
    if fnmatch(convert(i, 7), '?213*5664'):
        print(i, i // 333)

# otvet:
# 24888420 74740
# 371885742 1116774
# 654120891 1964327
# 937155573 2814281