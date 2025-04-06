from ctypes import c_int
from string import printable


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    num = 7**170 + 7**100 - x
    num = convert(num, 7)
    ans.append([num.count('0'), x])

print(max(ans))
