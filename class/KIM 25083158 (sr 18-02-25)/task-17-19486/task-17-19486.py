with open('17_19486.txt') as file:
    data = [int(i) for i in file]

count_7 = [i for i in data if str(i)[-1] == '7']
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    u1 = str(num1)[0] == '-'
    u2 = num2 > 0
    if u1 + u2 == 1 and num1 + num2 < len(count_7):
        ans.append(num1 + num2)
print(len(data), max(ans))

# otvet: 10000 -734