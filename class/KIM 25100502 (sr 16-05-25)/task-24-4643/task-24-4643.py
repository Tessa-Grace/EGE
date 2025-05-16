with open('24_4643.txt') as file:
    data = file.readline()

data = data.replace('B', 'A').replace('1', '*').replace('2', '*')

data= data.replace('**A', '!')

while '*' in data:
    data = data.replace('*', ' ')
while 'A' in data:
    data = data.replace('A', ' ')

data = data.split()

print(len(max(data, key=len)))

# otvet:67

#_____________________
from re import finditer

with open('24_4643.txt') as file:
    data = file.readline()

pattern = r'([12][12][AB])+'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(data, key=len))/3)