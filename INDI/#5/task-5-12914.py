ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r.replace('0', '11')
    else:
        r = r.replace('1', '10')
    r = int(r, 2)
    if r < 161:
        ans.append(r)
print(max(ans))

# otvet: 148