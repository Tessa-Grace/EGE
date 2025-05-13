with open('24_4602.txt') as file:
    data = file.readline()

for i in 'CD':
    data = data.replace(i, 'B')

data = data.replace('O', 'A')
data = data.replace('BA', '*')

for i in 'ABCD':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))

# otvet: 174