with open('24_10105.txt') as file:
    data = file.readline()

data = data.split('T')

ans = 0
for i in range(len(data) - 100):
    s = 'T'.join(data[i:i + 101])
    ans = max(ans, len(s))

print(ans)

# otvet: 133