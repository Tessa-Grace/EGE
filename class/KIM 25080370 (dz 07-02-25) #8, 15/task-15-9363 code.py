from itertools import permutations
from math import factorial

errors = [''.join(val) for val in permutations('ОУАЮЕ')]
print(factorial(12) - len(errors) * factorial(8))

# otvet: 474163200