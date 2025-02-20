#13820

def convert(n, sys):
    r = ''
    while n:
        r += str(n % 3)
        n //= 3
    return r[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if n % 7 == 0:
        r = r + r[-2:]
    else:
        r = r + convert(((n % 7) * 3), 3)
    r = int(r, 3)
    if r > 369:
        ans.append(r)
print(min(ans))

#Otvet: 384
