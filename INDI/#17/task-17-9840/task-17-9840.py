with open('17_9840.txt') as file:
    data = [int(i) for i in file]

max_39 = max(i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == '39')

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    if (u1 == True and u2 == False) or (u1 == False and u2 == True):
        if (num1 + num2) ** 2 <= max_39 ** 2:
            ans.append(num1 + num2)
print(len(ans), max(ans))

# otvet: 1591 9233
