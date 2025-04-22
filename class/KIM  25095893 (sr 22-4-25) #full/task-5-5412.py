from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

count = 0
for n in range(1, 10000):
    r = convert(n, 16)
    if r.count('b') % 2 == 0:
        r = '1' + r
    else:
        r += '1'
    r = int(r, 16)
    if 10 <= r <= 99:
        count += 1

print(count)

# otvet: 14