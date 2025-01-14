ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '100'
    else:
        r = r + '011'
    r = int(r, 2)
    if r > 300:
        ans.append(n)
print(min(ans))

#otvet: 38