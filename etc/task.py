from itertools import *
ans=[]
for r1 in range(3):
    for z1 in product('0123456789', repeat=r1):
        z1 = ''.join(z1)
        for r2 in range(3):
            for z2 in product('0123456789', repeat=r2):
                z2 = ''.join(z2)
                num = int(f'{z1}15{z2}7424')
                if num <= 10 ** 8:
                    u1 = num % 111 == 0
                    u2 = num % 113 == 0
                    u3 = num % 127 == 0
                    if u1 + u2 + u3 == 1:
                        ans.append([num, num // 111 if num % 111 == 0 else num // 113 \
                            if num % 113 == 0 else num // 127])


ans = sorted(ans)
for i in ans:
    print(*i)
