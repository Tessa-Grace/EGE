def triange(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def f(A):
    for x in range(1, 1000):
        tr1 = triange(A,7, x)
        maxx = max(x + 5, 14)
        tr2 = triange(36, 21, x)
        f = tr1 <= ((maxx <= 27) == (not tr2))
        if not f:
            return False
    return True

ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

#otvet: 50