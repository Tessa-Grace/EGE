def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 4)
    if len(r) % 2 == 0:
        r = r[:int(len(r)/2)] + '0' + r[int(len(r)/2):]
    r = int(r, 4)
    if r <= 180:
        ans.append(n)
print(max(ans))

# otvet: 63


'''
r = '123456'
r = r[:int(len(r)/2)] + '0' + r[int(len(r)/2):]
print(r) #1230456
'''
