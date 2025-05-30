with open('26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True) # или [::-1]

ans = [boxes[0]]
for box in boxes:
    if ans[-1] - box >= 3:
        ans.append(box)
print(len(ans), ans[-1])

# otvet: 2767 51

# или так:
# last = boxes[0]
# count = 1
#
# for box in boxes:
#     if last - box >= 3:
#         count += 1
#         last = box
#
# print(count, last)

