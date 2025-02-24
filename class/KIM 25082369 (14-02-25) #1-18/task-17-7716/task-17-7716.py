with open('17_7716.txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data if '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and \
        '6' not in str(i) and '8' not in str(i))

ans = []
for i in range(len(data) - 1):
    num1, num2 = str(data[i]), str(data[i+1])
    u1 = '1' not in num1 and '3' not in num1 and '5' not in num1 and \
         '7' not in num1 and '9' not in num1
    u2 = '1' not in num2 and '3' not in num2 and '5' not in num2 and \
         '7' not in num2 and '9' not in num2
    if u1 + u2 > 0 and int(num1) + int(num2) > maxx:
        ans.append(int(num1) + int(num2))
print(len(ans), max(ans))

# otvet: 56 18612
