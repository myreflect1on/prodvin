def print_products(*args):
    m = [i for i in args if type(i) == str and len(i)>1]
    if len(m) > 0:
        for i in range(len(m)):
            print(str(i+1)+') '+m[i], sep='\n')
    else:print('Нет продуктов')
print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
