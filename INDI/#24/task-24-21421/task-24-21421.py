from re import *
with open('24_21421.txt') as f:
    st = f.readline()

pattern  = r'[1-9AB][0-9AB]*[02468A]'
m = [i.group() for i in finditer(pattern, st)]
print(len(max(m, key=len)))

# otvet: 19

from string import ascii_uppercase

with open('') as file:
    data = file.readline()

for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')

data = data.split()
ans = 0
for i in data:
    i = i.rstrip('13579B').lstrip('0')
    ans = max(len(i), ans)

print(ans)

# otvet: 19