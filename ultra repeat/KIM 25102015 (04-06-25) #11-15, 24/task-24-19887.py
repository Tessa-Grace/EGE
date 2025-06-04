from re import *

with open('') as file:
    data = file.readline()

pattern = r'[13579]?([02468][13579])+[02468]?'
matches = finditer(pattern, data)

print(max(len(i.group()) for i in matches))
