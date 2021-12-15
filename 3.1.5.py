letters = ['a', 'b', 'c', 'd']
new_letters = []
#new_letters = new_letters.copy(letters)
new_letters2 = letters.copy()
new_letters3 = list(letters)
new_letters4 = letters[:]

print(new_letters)
print(new_letters2)
print(new_letters3)
print(new_letters4)

numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers)
words = ['xyz', 'zara', 'beegeek']
print(max(words))

list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]

print(min(list1))
print(max(list1))
print(min(list2))
print(max(list2))
list1 = [[1, 8, 9], [4, 8, 12, 16], [0, 2, 7]]
print(list1[0][1] + list1[1][2] + list1[2][2])

list1 = [[0, [9, 2]], [1, [4, 6, 3], [5, 2, 3], 8, 3]]
print(list1[1][2][1])
list1 = [[[1, 1, 0], [0, 1, 1]], [[0, 1], [1, 1], [1, 0]]]
list1 = [[1, 8, 7, 4], [1, 3, 4, 5, 6], [2, 7, 2], [2, 6, 7, 8]]
print(max(list1))