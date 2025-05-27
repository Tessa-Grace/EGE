with open('24_4544.txt') as file:
    data = file.readline()

data = data.replace('XIX', 'XI IX') # или на 'I I'
data = data.split()

print(len(max(data, key=len)))

# otvet: 293