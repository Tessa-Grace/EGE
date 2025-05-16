with open('24_2421.txt') as file:
    data = file.readline()

data = data.split('D')
print(len(max(data, key=len)))

# otvet: 44