with open('26.txt') as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

ans = [boxes[0]]
for box in boxes[1:]:
    if ans[-1] - box >= 9:
        ans.append(box)

print(len(ans),ans[-1])