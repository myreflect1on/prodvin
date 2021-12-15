def greet(t,*args):
    return 'Hello, '+t+'!' if len(args) == 0 else 'Hello, '+ t + ' and ' + ' and '.join(args)+'!'
print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))

