from re import *

with open('24_4627.txt') as file:
    data = file.readline()

pattern = '(NPO|PNO)+'

matches = finditer(pattern, data)

matches = [i.group() for i in matches]
print(len(max(matches, key=len)) // 3)

# otvet: 327
