with open('17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    if num1 % 16 == minn or num2 % 16 == minn:
        ans.append(num1 + num2)
print(len(ans), max(ans))

# otvet: 1214 176024