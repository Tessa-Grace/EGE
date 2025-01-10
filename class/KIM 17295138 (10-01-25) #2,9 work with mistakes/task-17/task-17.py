with open('task-17.txt') as file:
    arr = [int(i) for i in file]

max_68 = max([i for i in arr if str(i)[-2:] == '68'])

ans = []
for i in range(len(arr) - 3):
    n1, n2, n3, n4 = arr[i], arr[i+1], arr[i+2], arr[i+3]
    summ = n1 + n2 + n3+ n4
    u1 = 10 <= abs(n1) <= 99
    u2 = 10 <= abs(n2) <= 99
    u3 = 10 <= abs(n3) <= 99
    u4 = 10 <= abs(n4) <= 99
    f1 = u1 + u2 + u3 + u4 == 1
    f2 = u1 * u2 * u3 * u4
    f3 = summ >= max_68
    if (f1 or f2) and f3:
        ans.append(summ)

print(len(ans), max(ans))

