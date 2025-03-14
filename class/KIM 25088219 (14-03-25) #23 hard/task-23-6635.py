# ______________________________________________________________
#                            1 METHOD
# ______________________________________________________________
def f(cur, count=0):
    if count == 13 and cur < 0:
        ans.append(cur)
        return 1
    if count == 13 and cur >= 0:
        return 0
    return f(cur - 3, count + 1) + f(cur * (-3), count + 1)

ans = []
print(f(333), len(set(f(333))))
# ______________________________________________________________
#                            2 METHOD
# ______________________________________________________________
def f(cur, count=0):
    if count == 13 and cur < 0:
        return {cur}
    if count == 13 and cur >= 0:
        return set()
    return f(cur - 3, count + 1) | f(cur * (-3), count + 1)

print(len(f(333)))

# otvet: 2224