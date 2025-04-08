from string import ascii_uppercase

with open('2422.txt') as file:
    data = file.readline()

for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')

data = data.split()

ans = []
for i in data:
    i = i.strip('13579B')
    i = i.lstrip('0')
    ans.append(len(i))

print(max(ans))

