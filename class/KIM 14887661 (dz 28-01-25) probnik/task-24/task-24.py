with open('24_8510.txt') as file:
    data = file.readline()

while 'NN' in data or 'OO' in data or 'PP' in data:
    data = data.replace('NN', '*').replace('OO', '*').replace('PP', '*')

data = data.split('*')

print(len(max(data, key=len)))


# otvet: 140