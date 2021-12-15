func = lambda x: str(x[0]).lower() == str(x[-1]).lower() and str(x[0]) == 'a'
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bfrefrB'))
print(func('abcdA'))
