from functools import lru_cache

ans = []

@lru_cache(None)
def f(num, end=0, a=False, b=False, c= False):
    if end == 24:
        ans.append(num)
        return
    if num in ans:
        return
    if a:
        f(num + 7, end + 1, a=False, b=True, c=False)
        f(num * 4, end + 1, a=False, b=False, c=True)
    if b:
        f(num + 1, end + 1, a=True, b=False, c=False)
        f(num * 4, end + 1, a=False, b=False, c=True)
    if c:
        f(num + 7, end + 1, a=True, b=False, c=False)
        f(num + 1, end + 1, a=True, b=False, c=False)

    f(num + 7, end + 1, a=False, b=True, c=False)
    f(num + 1, end + 1, a=True, b=False, c=False)
    f(num * 4, end + 1, a=False, b=False, c=True)

f(1)
print(len(set(ans)))

# otvet: NET OTVETA