with open('24_3792.txt') as file:
    data = file.readline()


data = data.replace('D', ' ').replace('E', ' ')

data = data.split()
print(len(max(data, key=len)))

# otvet: 16