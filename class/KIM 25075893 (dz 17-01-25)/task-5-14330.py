ans = []
for num in range(10_000, 100_000):
    num = str(num)
    kv = (int(min(num)) + int(max(num))) ** 2
    mult = 1
    for i in num:
        if int(i) % 2 == 0:
            mult *= int(i)
    if kv < mult:                          # ans = str(max(kv, mult)) + str(min(kv, mult))
        res = str(mult) + str(kv)
    else:
        res = str(kv) + str(mult)
    if res == '12116':
        ans.append(num)
print(min(ans))

# otvet: 22229

