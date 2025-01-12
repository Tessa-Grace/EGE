ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if len(r) % 2 == 0:
        r += '1'
    else:
        r = '1' + r + '0'
    r = int(r, 2)
    if r > 666:
        ans.append(r)
print(min(ans))

# otvet: 1025