
l = {'foo': 100, 'bar': 200, 'baz': 300}
d = dict([('foo', 100), ('bar', 200), ('baz', 300)])

b = dict(foo=100, bar=200, baz=300)

c = {('foo', 100), ('bar', 200), ('baz', 300)}
print(l)
print(d)
print(b)
print(c)
data = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]
print(data)
d = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

print('z' in d[2])

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153}

recipients.update([('Scripps', 131), ('Math', 3456)])
print(recipients)