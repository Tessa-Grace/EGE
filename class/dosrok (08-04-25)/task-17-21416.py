with open('17.txt') as file:
    data = [int(i) for i in file]

minus = sum(i for i in data if i < 0)

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    sp = [num1, num2, num3]
    if max(sp) * min(sp) > minus:
        ans.append(num1 + num2 + num3)
print(len(ans), abs(max(ans)))

# otvet: 10007 7953