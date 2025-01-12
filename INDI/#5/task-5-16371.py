ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + bin((n % 3) * 3)[2:]
    r = int(r, 2)
    if r >= 195:
        ans.append(r)
print(min(ans))

# otvet: 199