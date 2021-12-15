numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1
print(result)

info = {'name': 'Bob',
        'age': 25}

name1 = info.setdefault('name')           # параметр default не задан
name2 = info.setdefault('name', 'Max')    # параметр default задан

print(name1)
print(name2)