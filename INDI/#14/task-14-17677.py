# 17677

def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for x in range(1, 2030):
    n = 6**260 + 6**160 + 6**60 - x
    r = convert(n, 6)
    if r.count('0') == 202:
        ans.append(x)
print(max(ans))

# otvet: 1944

