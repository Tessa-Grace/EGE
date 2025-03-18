from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 100000):
    r = convert(n, 12)
    if n % 3 == 0:
        r = '1' + r + 'B'
    else:
        r = '2' + r + '0'
    r = int(r, 12)
    if r < 1996:
        ans.append(r)
print(max(ans))

# otvet: 1991
