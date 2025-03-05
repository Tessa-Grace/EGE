a = 1_222_222_222 // 32
b = 1_555_555_666 // 32

ans = []
for n in range(a, b + 1):
    r = bin(n)[2:]
    r += ('000' + bin(n % 3)[2:])[-2:]
    r_10 = int(r, 2)
    r += ('000' + bin(r_10 % 5)[2:])[-3:]
    r = int(r, 2)
    if 1_222_222_222 <= r <= 1_555_555_666:
        ans.append(r)
print(len(ans))

# otvet: 10416669