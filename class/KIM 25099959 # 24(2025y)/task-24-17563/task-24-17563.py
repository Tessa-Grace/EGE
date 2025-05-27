from re import *

with open('24_17563.txt') as file:
    data = file.readline()
pattern = r'([7-9][0789]*[-*])+[7-9][0789]*'

matches = finditer(pattern, data)
matches = [match.group() for match in matches]
print(len(max(matches, key=len)))

# otvet: 40