num = 16807**35 + 2401**2 * 343**9 - 49**52 + 7**3 - 2005

count = 0
while num:
    if num % 49 > 9:
        count += 1
    num //= 49
print(count)

# otvet: 51