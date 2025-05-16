def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 10000):
    num = 6**900 + 6**10 - x
    num = convert(num, 6)
    if num.count('3') == num.count('5'):
        ans.append(x)
print(max(ans))

# otvet: 9591