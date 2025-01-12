ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    for i in range(2):
        r = r + str(sum(map(int, r)) % 2)
    r = int(r, 2)
    if r > 75:
        ans.append(r)
print(min(ans))

# otvet: 78
