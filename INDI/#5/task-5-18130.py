ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = '1' + r[:-2] + '11'
    else:
        r = '10' + r + '0'
    r = int(r, 2)
    if r > 999 and n % 2 == 0:
        ans.append(r)
print(min(ans))

# otvet: 1007