# 18578

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 4)
    if n % 4 == 0:
        r = '2' + r + '03'
    else:
        r = r + convert(((n % 4) * 5), 4)
    r = int(r, 4)
    if r <= 567:
        ans.append(n)
print(max(ans))

# otvet: 34