def f(cur, fin, count=0):
    if cur % 2 == 0: count += 1
    if cur == fin and count <= 15: return 1
    if cur > fin: return 0
    return f(cur + 2, fin, count) + \
        f(cur + 3, fin, count) + \
        f(cur * 2 + 1, fin, count)
print(f(1, 55))

# otvet: 4197234