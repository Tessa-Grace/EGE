with open('26_10107.txt') as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], -x[0]))

approved_events = [events[0]]
for event in events:
    if approved_events[-1][1] <= event[0]:
        approved_events.append(event)

print(len(approved_events), approved_events[-2:])
print(events[events.index(approved_events[-1]):])

# 32 [[1264, 1273], [1288, 1298]] => time=1298-1273=15(min)
# [[1288, 1298], [821, 1298], [653, 1299]] -




