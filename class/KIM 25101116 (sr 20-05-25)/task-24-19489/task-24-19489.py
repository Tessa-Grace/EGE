with open('24_19489.txt') as file:
    data = file.readline()

data = data.replace('WSFWW', 'WSFW SFWW')
data = data.split()

ans = []
for i in data:
    if i.count('WWF') <= 120:
        ans.append(i)
print(len(max(data, key=len)))

# otvet: 3080