from re import *

with open('24_18147.txt') as file:
    data = file.readline()

pattern = r'[7-9]+([+][7-9]+)+'
matches = finditer(pattern, data)

print(max(eval(i.group()) for i in matches))
