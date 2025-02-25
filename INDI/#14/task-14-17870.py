#17870

ans = []
for x in range(1,2031):
    n = 7**170 + 7**100 - x
    res = ''
    while n:
        res += str(n % 7)
        n //= 7
    res = res[::-1]
    if res.count('0') == 71:
        ans.append(x)
print(max(ans))

#otvet: 2029