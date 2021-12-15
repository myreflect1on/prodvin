print((lambda x: (x + 3) * 5 / 2)(3))
data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
result = list(map(lambda x: '.'.join(x), data))
print(result[1])
result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))

print(result)

files = ['duwwouy440.py', 'crocst0sse.cs', 'j9t7ga2s6x.java', 'jk4nnes4tp.py', '2spc9uqzhu.doc',
         'qi0ujxe0c7.png', 'z5x7l1j1d8.jpg', 'i5wtdxh366.geo', 'h53s2m2p73.py', 'ojty11f02d.sx',
         'jyjuwlvwb3.st', 'gv4940lf8m.txt', 'op38fy9m9x.docx', 'o02ltr8vbp.xlsx', 'la97gc4js4.html',
         'lcihrp8c6l.py', 'z66y7dgfo1.py', 'ckoks0849e.csv']

result = list(filter(lambda s: s.endswith('.py'), files))

print(len(result))
print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))
from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers)
print(result)
from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda a, b: a * b, numbers, 10)
print(result)

from functools import reduce

words = ['beegeek', 'stepik', 'python', 'iq-option']
result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(result)

from functools import reduce

result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
print(result)
from functools import reduce
import operator

def flatten(data):
    return reduce(operator.concat, data, [])

result = flatten([[1, 2], [3, 4], [], [5]])

print(result)