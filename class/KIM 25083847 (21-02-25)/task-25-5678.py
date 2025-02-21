from itertools import product

ans = []

for r1 in range(3):
    for z1 in product('0123456789', repeat=r1):
        z1 = ''.join(z1)
        for r2 in range(3 - r1):
            for z2 in product('0123456789', repeat=r2):
                z2 = ''.join(z2)
                num = int(f'124{z1}5{z2}79')
                summ = 0
                for i in str(num):
                    if i in '13579':
                        summ += int(i)
                if num <= 10 ** 8 and num % summ == 0:
                    ans.append([num, num // summ])

ans = sorted(ans)
for i in ans:
    print(*i)

# otvet:
# 1249579 40309
# 12409579 400309
# 12452979 401709
# 12456179 541573
