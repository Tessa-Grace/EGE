num = int(input())
ans = []
while num != 0:
    if num % 8 == 0:
        ans.append(num)
    num = int(input())
if len(ans) > 0:
    print(sum(ans) / len(ans))
else:
    print('NO')
