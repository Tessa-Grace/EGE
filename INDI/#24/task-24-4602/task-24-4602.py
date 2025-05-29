from re import *

with open('24_4602.txt') as file:
    data = file.readline()

pattern = r'([BCD][AO])+'

matches = finditer(pattern, data)

matches = [i.group() for i in matches]
print(len(max(matches, key=len)) // 2)

# otvet: 174

from re import *
with open('24_4602.txt') as f:
    st = f.readline()
pattern = r'([BCD][AO])+'
match = finditer(pattern, st)
m = [i.group() for i in match]
print(len(max(m, key=len))//2)
# otvet: 174