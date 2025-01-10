def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for n in range(11, 10000):
    r = convert(n, 3)


    chet = 0
    nechet = 0
    for i in r:
        if int(i) % 2 == 0:
            chet += 1
        else:
            nechet += 1

    if chet > nechet:
        r = '22' + r
    else:
        r = '11' + r

    r = int(r, 3)
    if r > 100:
        ans.append(r)
print(min(ans))

# otvet: 120
