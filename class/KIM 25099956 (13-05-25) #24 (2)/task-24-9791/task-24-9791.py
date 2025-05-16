# Усложненное условие:
# Найдите длину самого длинного 16-ричного числа,
# которое в 10-ричной с/с делится на 6 без остатка

from string import ascii_uppercase

with open('24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace('i', ' ')

data = data.split()

ans = 0
for i in data:
    i = i.lstrip('0')
    if int(i, 16) % 6 == 0:
        ans = max(ans, len(i))
    else:
        for l in range(len(i)):
            for r in range(len(i), l, -1):
                ps = i[l:r]
                if int(ps, 16) % 6 == 0:
                    ans = max(ans, len(i))
                    break
# Если в задании просят найти самое длинное число, кратное N,
# то мы должны помнить, что внутри каждой неподходящей подстроки,
# может скрываться более короткая подстрока, которая подойдет под условие
print(ans)

