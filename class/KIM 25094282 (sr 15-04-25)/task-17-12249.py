with open('17_12249.txt') as file:
    data = [int(i) for i in file]

max_3 = max(i for i in data if len(str(abs(i))) == 5 and abs(i) % 10 == 3)

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]

    u1 = abs(num1) % 10 == 3
    u2 = abs(num2) % 10 == 3
    u3 = abs(num3) % 10 == 3

    if u1 + u2 + u3 >= 1 and (num1 + num2 + num3) <= max_3:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

# otvet: 1767 99081
