print(any([True, False]))
print(any([False, False]))
print(any([True, True]))
print(any([10, 100, 1000]))
print(any([0, 0, 0, 0]))
print(any(['Python', 'C#']))
print(any(['', '', 'language']))
print(any([(1, 2, 3), []]))
print(any([]))
print(any([[], []]))
print(any({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'}))
print(any({0: 'Monday'}))
print(any({'name': 'Timur', 'age': 28}))
print(any({'': 'None', 'age': 28}))
numbers = [10, 30, 20, 50, 40, 60, 70, 80]

total = 0
for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        total += number
print(total)
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

result = 0
for x, y in zip(list1, list2):
    result += x*y
print(result)