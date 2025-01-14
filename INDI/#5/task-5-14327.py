ans = []
for n in range(1, 10000):
    r = oct(n)[2:]
    if n % 2 == 0:
        r = r + max(r)
    else:
        r = r + oct(int(min(r)) * 2)[2:]
    r = int(r, 8)
    if r < 313:
        ans.append(n)
print(max(ans))

# otvet: 38
