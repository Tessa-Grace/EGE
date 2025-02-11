with open('17_9748.txt') as file:
    data = [int(i) for i in file]

max_15 = max([i for i in data if str(i)[-2:] == '15'])
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    if (len(str(abs(num1))) == 4) + (len(str(abs(num2))) == 4) + \
            (len(str(abs(num1))) == 4) == 1:
        if num1 + num2 + num3 >= max_15:
            ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

# otvet: 111 196183