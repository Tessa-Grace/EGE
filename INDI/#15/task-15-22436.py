def f(a):
    for x in range(1, 10000):
        f = ((35 <= x <= 66) <= ((x+1) % 17 != 0)) or (x % a == 0)
        if not f:
            return False
    return True
ans=[]
for a in range(1, 10000):
    if f(a):
        ans.append(a)
print(max(ans))

#otvet: 50