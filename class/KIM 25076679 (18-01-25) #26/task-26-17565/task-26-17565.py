with open('26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    students = []
    for line in file:
        line = line.split()
        id = str(line[0])
        result = sum(map(int, line[1:4]))
        sobes = int(line[-1])
        students.append([id, result, sobes])

students = sorted(students, key=lambda x: (-x[1], -x[2], x[0]))
ball = sum([i[1] for i in students]) / N

ans1 = 0
ans2 = 0
for student in students[:S]:
    if student[1] >= ball:
        ans1 = students[0]
    else:
        ans2 += 1
print(ans1, ans2)

