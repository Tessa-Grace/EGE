with open('24_1866.txt') as file:
    data = file.readline()

while 'ad' in data:
    data = data.replace('ad', 'a d')

while 'da' in data:
    data = data.replace('da', 'd a')

data = data.split()
print(len(max(data, key=len)))


# otvet: 2252