def f(cur, fin, count=0):
    if cur == fin and count == 51: return 1
    if cur > fin: return 0
    return f(cur * 4, fin, count + 1) + \
        f(cur + 1, fin, count + 1) + \
        f(cur * 3, fin, count + 1) # увеличиваем число, тк оно каждый раз будет различным

print(f(2, 404))

# otvet: 319