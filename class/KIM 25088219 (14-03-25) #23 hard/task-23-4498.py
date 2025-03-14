def f(cur, fin, count_1=0, count_2=0, count_3=0):
    if cur == fin and count_1 <= 4 and count_2 >= 2 and count_3 == 5: return 1
    if cur > fin: return 0
    return f(cur * 5, fin, count_1 + 1, count_2, count_3) + \
        f(cur * 3, fin, count_1, count_2 + 1, count_3) + \
        f(cur + 45, fin, count_1, count_2, count_3 + 1)
print(f(1, 2970))

# otvet: 74