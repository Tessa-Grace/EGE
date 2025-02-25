from itertools import product

ans = []
for A in '02468':
    for i in range(4):
        for B in product('13579', repeat=i):
            B = ''.join(B)
            num = int('1' + A + '2157' + B + '4')
            if num % 133 == 0:
                ans.append([num, num // 133])

ans = sorted(ans)
for i in ans:
    print(*i)

# otvet:
# 122157574 918478
# 1021575394 7681018
# 1421575554 10688538
# 1821575714 13696058

