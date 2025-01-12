ans = []
for n in range(1, 12):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '10'
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    ans.append(r)
print(max(ans))

# otvet: 109