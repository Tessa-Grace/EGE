with open('24_4682.txt') as file:
    data = file.readline()

for i in 'CD':
    data = data.replace(i, 'B')

data = data.replace('E', 'A')
data = data.replace('AB', '*')

for i in 'ABCD':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))

# otvet: 202