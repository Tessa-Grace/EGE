#18122

ans = []
for x in range(1, 5556):
    num = 5**150 + 5**135 - x
    res = ''
    while num:
        res += str(num % 5)
        num //= 5
    res = res[::-1]
    if res.count('4') == 134:
        ans.append(x)
print(max(ans))

# otvet: 3126