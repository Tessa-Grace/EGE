from string import ascii_uppercase

data = ''
for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')

data = data.split()

ans = []
for i in data:
    i = i.strip('13579B')
    i = i.lstrip('0')
    ans.append(len(i))

print(max(ans))

