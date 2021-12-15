def arithmetic_operation(x):
    if x == '+':
        return (lambda a, b: a + b)
    if x == '/':
        return (lambda a, b: a / b)
    if x == '*':
        return (lambda a, b: a * b)
    if x == '-':
        return (lambda a, b: a - b)




add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))