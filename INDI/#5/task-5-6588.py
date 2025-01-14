ans = []
for n in range(1, 100):
    r = bin(n)[2:]
    r = r.replace('0', '*')
    r = r.replace('1', '0')
    r = r.replace('*', '1')
    r = '1' + r
    if r.count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    r = int(r, 2)
    if r > 180:
        ans.append(n)
print(min(ans))

# otvet: 32