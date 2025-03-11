ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        ost = (n % 3) * 3
        r += bin(ost)[2:]
    r = int(r, 2)
    if r > 76:
        ans.append(n)
print(min(ans))

# otvet: 11