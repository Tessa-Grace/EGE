def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

chet = [i for i in range(5) if i % 2 == 0]
nechet = [i for i in range(5) if i % 2 != 0]

ans = []
for x in range(1, 2006):
    num = convert(43**56 + 113**841 - x, 4)
    ch = []
    nch = []
    for i in num:
        if int(i) in chet: ch.append(i)
        else: nch.append(i)
    if len(ch) % 2 == 0 and len(nch) % 2 == 0 and num.count('2') <= 712:
        ans.append(x)
print(max(ans))

# otvet: 2001