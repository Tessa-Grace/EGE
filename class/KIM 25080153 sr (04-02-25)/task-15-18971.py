def f(A):
     for x in range(1, 1000):
         for y in range(1, 1000):
             f = (y > 10) or (x * A > y + x)
             if not f:
                 return False
     return True

ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(min(ans))

# otvet: 12
