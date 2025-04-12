from re import findall

with open('24_1866.txt') as file:
    data = file.readline()

pattern = r'(?<=ad|da)\w+?(?=ad|da)'
matches = findall(pattern, data)
print(len(max(matches, key=len)) + 2)

# otvet: 2252