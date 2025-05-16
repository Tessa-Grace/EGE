with open('24_17535.txt') as file:
    data = file.readline()

data = data.split('CD')

ans = 0
for i in range(len(data) - 160):
    s = 'CD'.join(data[i:i + 161])
    ans = max(ans, len(s) + 2)

print(ans)

# otvet: 9712