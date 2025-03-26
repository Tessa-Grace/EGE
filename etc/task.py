students = int(input())
count_students = 0
maxx = 0
ans = []
while count_students != students :
    q = int(input())
    count_students += 1
    ans.append(q)
    maxx = max(ans)

print(maxx)
if ans.count(0) > 0:
    print('YES')
else:
    print('NO')