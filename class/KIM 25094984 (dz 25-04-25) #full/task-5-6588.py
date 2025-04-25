for n in range(1, 10000):
    r = bin(n)[2:]
    r = r.replace('0', '*')
    r = r.replace('1', '0')
    r = r.replace('*', '1')
    r = '1' + r
    if r.count('1') % 2 != 0:
        r += '1'
    else:
        r += '0'
    r = int(r, 2)
    if r > 180:
        print(n)
        break
# otvet: 32