ans = []
for x in range(2, 2026):
    num = 5**2025 + 5**200 - x
    count = 0
    while num:
        if num % 5 == 4:
            count +=1
        num //= 5
    ans.append([count, x])

print(max(ans))

# [199, 1876]
# otvet: 1876

#ver. 2
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(2, 2026):
    num = 5**2025 + 5**200 - x
    count = convert(num, 5).count('4')
    ans.append([count, x])

print(max(ans))
# [199, 1876]
# otvet: 1876