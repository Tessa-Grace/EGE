with open('24_3228.txt') as file:
    data = file.readline()

data = data.replace('AC', '*').replace('AB', '*')
for i in 'ABC':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))

# otvet: 19