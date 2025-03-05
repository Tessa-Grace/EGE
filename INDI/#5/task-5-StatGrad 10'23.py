a = 1_111_111_110 // 32
b = 1_444_444_416 // 32

ans = []
for n in range(a, b + 1):
    r = bin(n)[2:]
    r += ('000' + bin(n % 3)[2:])[-2:]
    r_10 = int(r, 2)
    r += ('000' + bin(r_10 % 5)[2:])[-3:]
    r = int(r, 2)
    if 1_111_111_110 <= r <= 1_444_444_416:
        ans.append(r)
print(len(ans))

# otvet: 10416665