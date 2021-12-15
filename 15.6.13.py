from operator import*
from functools import reduce

result = reduce(add, range(1, 6))
print(result)