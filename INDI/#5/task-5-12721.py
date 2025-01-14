ans = []
for n in range(1, 10000):
    r = oct(n)[2:]
    if (r.count('0') + r.count('2') + r.count('4') + r.count('6')) % 2 > 0:
        r = r[-3:] + '46'
    else:
        r = oct(int(n % 8) * 5)[2:] + r
    r = int(r, 8)
    if n >= 80:
        ans.append(r)
print(min(ans))

# otvet: 38