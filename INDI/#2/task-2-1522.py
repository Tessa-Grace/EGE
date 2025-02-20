from itertools import *

def f(x, y, z):
    return (x <= z) and (y <= x)

table = [(1, 0, 0), (1, 1, 0)]

for p in permutations('xyz'):
    if [f(**dict(zip(p, r))) for r in table] == [1, 1]:
        print(p)

#('z', 'x', 'y')  
# 
# 
#    

