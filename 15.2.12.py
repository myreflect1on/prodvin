def mean(*args, **kwargs):
    m = []
    for i in args:
        if type(i) in (int, float):
            m.append(i)
    if len(m) != 0:
        return sum(m)/len(m)
    else:return 0.0
print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
