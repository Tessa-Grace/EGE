from re import *

with open('24_1866.txt') as file:
    data = file.readline()

pattern = r'(?<=ad|da)\w+?(?=ad|da)'

matches = finditer(pattern, data)

matches = [i.group() for i in matches]
print(len(max(matches, key=len)) + 2)

# otvet: 2252