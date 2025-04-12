with open('17_6791.txt') as file:
    data = [int(i) for i in file]

min_68 = min(i for i in data if str(i)[-2:] == '68')
# print(min_68)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]

    u1 = str(num1) == '68'
    u1_2 = str(num2) == '68'
    u2 = num1 ** 2 + num2 ** 2 >= min_68 ** 2

    if u1 + u1_2 == 1 and u2:
        ans.append(num1 ** 2 + num2 ** 2)
print(len(ans), max(ans))

# ANS IS EMPTY
# MISTAKE