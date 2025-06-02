from re import *

with open('24_12111.txt') as file:
    data = file.readline()

pattern = '(HPY|NYN)+'

matches = finditer(pattern, data)

matches = [i.group() for i in matches]
print(len(max(matches, key=len)) // 3)

# otvet: 16
