def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        summ = sum(map(int, r))
        summ = convert(summ, 3)
        r = r + summ
    r = int(r, 3)
    if r > 220 and r % 2 == 0:
        ans.append(r)
print(min(ans))

#otvet: 222
