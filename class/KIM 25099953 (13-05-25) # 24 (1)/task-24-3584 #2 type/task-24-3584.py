with open('24_3584.txt') as file:
    data = file.readline()

data = data.replace('BA', '*').replace('DA', '*')
for i in 'ABD':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))

# otvet: 151